from enum import Enum
from .format import get_frames_with_seq, get_frames_with_header, DataSet, frame_to_dict, check_frames
from loguru import logger
from .log import log_init
from functools import partial
import pandas as pd
log_init()



def parse_file(file_path:str, type: Enum, set:DataSet= DataSet.SCI):
    with open(file_path, "rb") as f:
        data = f.read()
    try:
        frames = get_frames_with_seq(data, type)
    except Exception as e:
        logger.warning(f"Failed to parse file {file_path} with {type} Seq, trying to parse with frame specified by header: {e}")
        frames = get_frames_with_header(data, type)
    frames_checked = check_frames(frames, type)
    dicts = map(partial(frame_to_dict, type=type, set=set), frames_checked)

    df = pd.DataFrame(dicts)
    return df