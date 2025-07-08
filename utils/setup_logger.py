import logging
import os
from logging.handlers import TimedRotatingFileHandler


def setup_logger(logger_name: str = "FastAPI SDK", log_dir: str = "logs"):
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.INFO)
    log_format = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    if not logger.handlers:
        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(log_format)
        logger.addHandler(ch)

        # File Handler
        os.makedirs(log_dir, exist_ok=True)
        file_handler = TimedRotatingFileHandler(
            filename=f"{log_dir}/{logger_name}.log",  # 로그 파일 이름
            when="midnight",  # 자정마다 새 로그 생성
            interval=1,  # 1일 간격
            backupCount=7,  # 최근 7일 로그 보관
            encoding="utf-8",
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger
