from collections import deque
from datetime import datetime as dt

from data_validation import LogValidation
from logger import logger


class UserEvent:
    """
    Calculates total session and duration for each user per day
    :returns Username, Total sessions, Session Duration
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.user_sessions = {}
        self.user_session_count = {}
        self.user_session_duration = {}
        self.earliest_time = None
        self.latest_time = None
        self.timestamp_str = None
        self.username = None
        self.marker = None

    def check_file_extension(self) -> bool:
        """Checks if the file exists and ends with .txt extension."""
        if not self.filename.endswith(".txt"):
            logger.error(
                f"File '{self.filename}' does not "
                f"end with .txt extension."
            )
            return False

        return True

    def check_valid_log_entry_data(self) -> bool:
        """
        Checks validity of input data.
        Log entry data: timestamp_str, username, marker
        :returns bool
        """
        log_data = LogValidation(self.timestamp_str, self.username, self.marker)
        valid_entry_data = log_data.is_valid_data
        return valid_entry_data

    def process_data(self) -> None:
        self.timestamp_str = dt.strptime(self.timestamp_str, "%H:%M:%S")
        self.update_timestamp_and_time_range()
        self.create_user_sessions()
        self.add_user_session()

    def update_timestamp_and_time_range(self) -> None:
        """Updates timestamp and time range."""
        if self.earliest_time is None or self.timestamp_str < self.earliest_time:
            self.earliest_time = self.timestamp_str

        if self.latest_time is None or self.timestamp_str > self.latest_time:
            self.latest_time = self.timestamp_str

    def create_user_sessions(self) -> None:
        """
        Creates user sessions and initializes
        session count and duration.
        """
        if self.username not in self.user_sessions:
            self.user_sessions[self.username] = deque()

            # Add username to user_session_count
            self.user_session_count[self.username] = 0
            self.user_session_duration[self.username] = 0

    def add_user_session(self) -> None:
        """Adds a new user session based on the marker."""
        if self.marker.lower() == "start":
            self.user_sessions[self.username].append([self.timestamp_str, None])
        elif self.marker.lower() == "end":
            self.handle_end_marker()

    def handle_end_marker(self) -> None:
        """Handles the 'End' marker."""
        if (
            not self.user_sessions.get(self.username)
            or self.user_sessions[self.username][-1][1] is not None
        ):
            self.user_session_duration[self.username] += (
                self.timestamp_str - self.earliest_time
            ).seconds

            self.user_session_count[self.username] += 1

        elif self.user_sessions[self.username] is not None:
            if None in self.user_sessions[self.username][0]:
                self.user_sessions[self.username][0][-1] = self.timestamp_str
                start_session, end_session = self.user_sessions[
                    self.username
                ].popleft()
                self.user_session_duration[self.username] += (
                    end_session - start_session
                ).seconds

                self.user_session_count[self.username] += 1

    def processing_file(self) -> None:
        """Processes data line by line from input filename."""
        try:
            with open(self.filename) as file:
                for line in file:
                    parts = line.strip().split()

                    try:
                        self.timestamp_str, self.username, self.marker = parts
                    except ValueError:
                        continue

                    # Checks if the 3 inputs are valid or not
                    valid_data = self.check_valid_log_entry_data()

                    if valid_data:
                        self.process_data()

        except FileNotFoundError:
            logger.error(f"File '{self.filename}' does not exist.")
            print(f"File '{self.filename}' does not exist.")

    def generate_report(self) -> None:
        """
        Adds/ Retrieves session count and duration time for each user.
        :returns user_name, session_count, total_duration
        """
        for user_name in self.user_sessions:
            total_duration = self.user_session_duration[user_name]
            session_count = self.user_session_count[user_name] + len(
                self.user_sessions[user_name]
            )
            print(f"{user_name} {session_count} {total_duration}")
