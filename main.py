import sys

from event import UserEvent


def app(filename: str) -> None:
    """Generates report based on UserEvent class."""
    event = UserEvent(filename)

    if event.check_file_extension():
        event.processing_file()
        event.generate_report()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    log_file_name = sys.argv[1]
    app(log_file_name)
