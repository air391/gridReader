from enum import Enum
from typing import Iterable

import featseq
import hkseq
import pandas as pd
import waveseq
from kaitaistruct import KaitaiStruct
from loguru import logger
from time import time
logger.add("parse.log", level="DEBUG")

class DataType(Enum):
    WAVE = 0
    FEAT = 1
    HK = 2


WAVE = DataType.WAVE
FEAT = DataType.FEAT
HK = DataType.HK


def frame_to_dict(frame: KaitaiStruct, keys: list[str]) -> dict:
    d = {}
    for k in keys:
        d[k] = getattr(frame, k)
    return d
def get_frames(seq: KaitaiStruct) -> Iterable[KaitaiStruct]:
    if isinstance(seq, hkseq.Frameseq):
        return (f_with_noise.frame for f_with_noise in seq.frames)
    else:
        return (f for f in seq.frames)


def get_keys(seq: KaitaiStruct) -> list[str]:
    return [k for k in next(get_frames(seq)).__dict__.keys() if not k.startswith("_")]


def get_seq_cls(type: DataType):
    if type == WAVE:
        return waveseq.Frameseq
    elif type == FEAT:
        return featseq.Frameseq
    elif type == HK:
        return hkseq.Frameseq
    else:
        raise ValueError(f"Unknown data type: {type}")
def get_frm_cls(type: DataType):
    if type == WAVE:
        return waveseq.Frame
    elif type == FEAT:
        return featseq.Frame
    elif type == HK:
        return hkseq.Frame
    else:
        raise ValueError(f"Unknown data type: {type}")

def read_file(file_path: str, data_type: DataType) -> pd.DataFrame:
    cls = get_seq_cls(data_type)
    try:
        seq = cls.from_file(file_path)
        frames = get_frames(seq)
    except EOFError as e:
        logger.warning(f"{data_type} file {file_path} meet EOFError: {e}\n trying to use frame based parser")
        pass
        logger.critical("Unimplemented")
        raise
    keys = get_keys(seq)
    df = pd.DataFrame(map(lambda f: frame_to_dict(f, keys), frames))
    return df
if __name__ == "__main__":
    df = read_file(r"特征量模式\000_observe.dat", FEAT)
    print(df.info())
    t0 = time()
    df.to_csv("data/feature.csv")
    t1 = time()
    df1 = pd.read_csv("data/feature.csv")
    print(f"csv: wirte {t1-t0},read {time()-t1}")
    t0 = time()
    df.to_parquet("data/feature.parquet")
    t1 = time()
    df1 = pd.read_parquet("data/feature.parquet")
    print(f"parquet: wirte {t1-t0},read {time()-t1}")
    t0 = time()
    df.to_hdf("data/feature.hdf5", key="feature", mode="w")
    t1 = time()
    df1 = pd.read_hdf("data/feature.hdf5", key="feature")
    print(f"hdf5: wirte {t1-t0},read {time()-t1}")