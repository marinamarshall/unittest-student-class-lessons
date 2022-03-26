import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """
    TestStudent
    """
    def test_full_name(self):
        """
        test full name
        """
        student = Student("John", "Doe")

        self.assertEqual(student.full_name, "John Doe")


    def test_alert_santa(self):
        """
        test alert santa
        """
        student = Student("John", "Doe")
        student.alert_santa()

        self.assertTrue(student.naughty_list)


    def test_email(self):
        """
        test email
        """
        student = Student("John", "Doe")

        self.assertEqual(student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
