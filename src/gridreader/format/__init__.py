from . import feat_testB2412
from . import hk_testB2412
from . import tel_testB2412
from . import wave_testB2412
from enum import Enum
from kaitaistruct import KaitaiStruct
from ..log import log_init, logger
import re
log_init()


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


def get_frames_from_seq(seq: KaitaiStruct) -> list[KaitaiStruct]:
    match type(seq):
        case TestB2412.HK:
            return [f.frame for f in seq.frames]
        case [TestB2412.FEAT, TestB2412.HK, TestB2412.TEL, TestB2412.WAVE]:
            return seq.frames
        case _:
            raise Exception("Not implemented")


def get_frames_with_seq(bs: bytes, type: Enum) -> list[KaitaiStruct]:
    cls: KaitaiStruct = get_frameseq(type)
    try:
        seq = cls.from_bytes(bs)
    except Exception as e:
        logger.info(f"Parse with {type} Sequence Failed. Exception {e}, {e.args}")
        raise e
    frames = get_frames_from_seq(seq)
    return frames


def get_frames_with_header(bs: bytes, type: Enum) -> list[KaitaiStruct]:
    cls: KaitaiStruct = get_frame(type)
    header, length = get_header_length(type)
    pattern = re.compile(re.escape(header.to_bytes(len(header), "big")))
    matches = [m.start() for m in pattern.finditer(bs)]
    frames = []
    for match in matches:
        if match + length > len(bs):
            break
        data = bs[match : match + length]
        try:
            frames.append(cls.from_bytes(data))
        except Exception as e:
            logger.debug(f"Parse {data} with {type} Header Failed. Exception {e}, {e.args}")
    return frames