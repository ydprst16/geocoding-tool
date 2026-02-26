import logging
import colorlog
import os

def setup_logger(name="app"):
    os.makedirs("logs", exist_ok=True)

    logger = colorlog.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    console = colorlog.StreamHandler()
    console.setFormatter(colorlog.ColoredFormatter(
        "%(asctime)s | %(log_color)s%(levelname)s%(reset)s | %(message)s"
    ))

    file_handler = logging.FileHandler("logs/geocode.log", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    ))

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

def log_status(logger, message, status):
    if status == "SUCCESS":
        logger.info(message)

    elif status == "OUT_OF_KECAMATAN":
        logger.warning(message)

    elif status == "OUT_OF_DUMAI":
        logger.error(message)  # merah

    else:
        logger.error(message)