from . import feat_testB2412
from . import hk_testB2412
from . import tel_testB2412
from . import wave_testB2412
from enum import Enum
from kaitaistruct import KaitaiStruct
from ..log import log_init, logger
from typing import Iterable, Callable, Any
import re
import crc

log_init()


class DataSet(Enum):
    SCI = 0
    RAW = 1
    ALL = 2


class SharedAutoEnum:
    _counter = 0  # 全局计数器

    @classmethod
    def create_enum(cls, name, members):
        cls._counter += len(members)
        member_dict = {
            key: value
            for key, value in zip(
                members, range(cls._counter - len(members) + 1, cls._counter + 1)
            )
        }
        return Enum(name, member_dict)


# 创建枚举类
TestB2412 = SharedAutoEnum.create_enum("TestB2412", ["FEAT", "HK", "TEL", "WAVE"])
Test = SharedAutoEnum.create_enum("Test", ["FEAT"])


def get_mod(type: Enum) -> type:
    match type:
        case TestB2412.FEAT:
            return feat_testB2412
        case TestB2412.HK:
            return hk_testB2412
        case TestB2412.TEL:
            return tel_testB2412
        case TestB2412.WAVE:
            return wave_testB2412
        case _:
            raise Exception("Not implemented")


def get_frame(type: Enum) -> type:
    return get_mod(type).Frameseq.Frame


def get_frameseq(type: Enum) -> type:
    return get_mod(type).Frameseq


HEADER_LENGTH = 4


def get_header_length(type: Enum) -> tuple[int, int]:
    match type:
        case TestB2412.FEAT:
            return 0x1C1C2288, 528
        case TestB2412.HK:
            return 0x1A2B3C4D, 109
        case TestB2412.TEL:
            return 0x47524944, 73
        case TestB2412.WAVE:
            return 0x2E2E33FF, 560
        case _:
            raise Exception("Not implemented")


def get_frames_from_seq(seq: KaitaiStruct, type: Enum) -> list[KaitaiStruct]:
    match type:
        case TestB2412.HK:
            return [f.frame for f in seq.frames]
        case TestB2412.FEAT | TestB2412.HK | TestB2412.TEL | TestB2412.WAVE:
            return seq.frames
        case _:
            raise Exception("Not implemented")


crc16 = crc.Calculator(crc.Crc16.XMODEM, optimized=True)


def get_checker(type: Enum) -> Callable[[KaitaiStruct], bool]:
    match type:
        case TestB2412.TEL:
            return lambda f: f.sum == sum(f.body_data)
        case TestB2412.FEAT | TestB2412.WAVE:
            return lambda f: crc16.verify(bytes(f.body_data), f.crc)
        case TestB2412.HK:
            #TODO - HK data crc error
            return lambda f: True
        case _:
            raise Exception("Not implemented")

def get_frames_with_seq(bs: bytes, type: Enum) -> list[KaitaiStruct]:
    cls: KaitaiStruct = get_frameseq(type)
    try:
        seq = cls.from_bytes(bs)
    except Exception as e:
        logger.info(f"Parse with {type} Sequence Failed. Exception {e}, {e.args}")
        raise e
    frames = get_frames_from_seq(seq, type)
    return frames


def get_frames_with_header(bs: bytes, type: Enum) -> list[KaitaiStruct]:
    cls: KaitaiStruct = get_frame(type)
    header, length = get_header_length(type)
    pattern = re.compile(re.escape(header.to_bytes(HEADER_LENGTH, "big")))
    matches = [m.start() for m in pattern.finditer(bs)]
    frames = []
    fail_count = 0
    for match in matches:
        if match + length > len(bs):
            break
        data = bs[match : match + length]
        try:
            frames.append(cls.from_bytes(data))
        except Exception as e:
            fail_count += 1
            logger.debug(
                f"Parse {data} with {type} Header Failed. Exception {e}, {e.args}"
            )
    logger.info(
        f"Parse {type} with Header Failed {fail_count} times, got {len(frames)} frames"
    )
    return frames


def check_frames(frames: list[KaitaiStruct], type: Enum) -> Iterable[KaitaiStruct]:
    checker = get_checker(type)
    error_count = 0
    pass_count = 0
    for frame in frames:
        if checker(frame):
            pass_count += 1
            yield frame
        else:
            error_count += 1
            logger.trace(f"Frame {frame} with {type} Failed Checker")
    logger.info(
        f"Check {type} with Checker Failed {error_count} times, got {pass_count} frames"
    )

def frame_to_sci(frame: dict[str, Any], type: Enum) -> dict[str, Any]:
    match type:
        case TestB2412.TEL:
            return {
                f"sipm_temp{i}inC": frame[f"sipm_temperature_ch{i}"] / 100 - 273.15
                for i in range(4)
            }
        case TestB2412.HK:
            temps = {
                "sipm_temp{i}inC": frame[f"temperature_sipm_ch{i}"] / 100 - 273.15
                for i in range(4)
            }
            bias = {
                "sipm_bias{i}inV": frame[f"voltage_sipm_ch{i}"] * 1e-3 for i in range(4)
            }
            temps.update(bias)
            return temps
        case _:
            return {}


def frame_to_dict(frame: KaitaiStruct, type: Enum, set: DataSet) -> dict[str, Any]:
    raw = {k: getattr(frame, k) for k in frame.__dict__ if not k.startswith("_")}
    if set == DataSet.RAW:
        return raw
    sci = frame_to_sci(raw, type)
    if set == DataSet.SCI:
        return sci
    elif set == DataSet.ALL:
        return {**raw, **sci}
    else:
        raise Exception("Not implemented")
