import unittest

from src.event import UserEvent


class TestUserEvent(unittest.TestCase):

    def setUp(self):
        self.user_event = UserEvent("test_log.txt")

    def test_check_file_extension_valid(self):
        self.user_event.filename = "valid_filename.txt"
        self.assertTrue(self.user_event.check_file_extension())

    def test_check_file_extension_invalid(self):
        self.user_event.filename = "invalid_filename.csv"
        self.assertFalse(self.user_event.check_file_extension())


if __name__ == '__main__':
    unittest.main()
