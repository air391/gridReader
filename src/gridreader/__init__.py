from enum import Enum
from .format import get_frames_with_seq, get_frames_with_header
from kaitaistruct import KaitaiStruct
from loguru import logger
from .log import log_init
log_init()


def parse_file(file_path:str, type: Enum):
    with open(file_path, "rb") as f:
        data = f.read()
    try:
        frames = get_frames_with_seq(data, type)
    except Exception as e:
        logger.warning(f"Failed to parse file {file_path} with {type} Seq, trying to parse with frame specified by header: {e}")
        frames = get_frames_with_header(data, type)
    