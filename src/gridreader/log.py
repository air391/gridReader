from loguru import logger
import sys
def log_init():
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add("logs/debug.log", level="DEBUG", rotation="10 MB")
    logger.add("logs/info.log", level="INFO", rotation="10 MB")
    logger.add("logs/error.log", level="ERROR", rotation="10 MB")