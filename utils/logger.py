import logging
from pathlib import Path


class PlantMindLogger:
    """
        Singleton logger used throughout the project.
        """
    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is not None:
            return cls._logger

        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        logger = logging.getLogger("PlantMind")

        logger.setLevel(logging.INFO)

        logger.propagate = False

        if not logger.handlers:
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",

                datefmt="%Y-%m-%d %H:%M:%S"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            file_handler = logging.FileHandler(
                log_directory / "plantmind.log",

                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        cls._logger = logger

        return logger