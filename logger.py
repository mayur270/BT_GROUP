import logging


class LoggerConfig:

    def __init__(self, filename: str = "error_report.txt"):
        self.logger = logging.getLogger(__name__)
        self.filename = filename

    def configure_logger(self) -> None:
        """ Formatting logger """
        # Create a file handler
        file_handler = logging.FileHandler(self.filename)

        # Set the formatter
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(filename)s -"
            " Line %(lineno)s | %(message)s",
        )
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

        # Set the logging level to DEBUG
        self.logger.setLevel(logging.DEBUG)


# Create a LoggerConfig instance
logger_config = LoggerConfig()

# Configure the logger
logger_config.configure_logger()

# Use the logger
logger = logging.getLogger(__name__)
