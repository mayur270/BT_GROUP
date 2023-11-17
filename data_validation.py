from datetime import datetime as dt

from logger import logger


class LogValidation:
    """
    Input fields are validated in this class.
    They should be as follows:
    :timestamp_str: 'HH:SS:MM',
    :username: "GEORGE11" - Alphanumeric only,
    :marker: 'Start' or 'End'
    """
    def __init__(self, timestamp_str: str, username: str, marker: str):
        self.timestamp_str = timestamp_str
        self.username = username
        self.marker = marker.lower()

    @property
    def validate_timestamp(self) -> bool:
        """
        Checks timestamp format: HH:MM:SS
        :returns bool
        """
        try:
            dt.strptime(self.timestamp_str, "%H:%M:%S")
            return True
        except ValueError:
            return False

    @property
    def validate_username(self) -> bool:
        """
        Check username format: Only Alphanumeric
        :returns bool
        """
        return self.username.isalnum()

    @property
    def validate_marker(self) -> bool:
        """
        Checks start/end log for each user
        :returns bool
        """
        return self.marker in ("start", "end")

    @property
    def is_valid_data(self) -> bool:
        """
        Checks errors for all validation data
        :returns bool
        """
        errors = []

        if not self.validate_timestamp:
            errors.append("Invalid timestamp format")

        if not self.validate_username:
            errors.append("Username should be alphanumeric")

        if not self.validate_marker:
            errors.append("Marker should be 'start' or 'end'")

        if errors:
            logger.error(
                f"Invalid log entry: "
                f"{self.timestamp_str, self.username, self.marker}. "
                f"Errors: {errors}"
            )
            return False

        return True
