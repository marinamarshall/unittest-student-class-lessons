import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):
    """
    TestStudent
    """

    def setUp(self):
        self.student = Student("John", "Doe")


    def test_full_name(self):
        """
        test full name
        """
        self.assertEqual(self.student.full_name, "John Doe")


    def test_alert_santa(self):
        """
        test alert santa
        """
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        """
        test email
        """
        self.assertEqual(self.student.email, "john.doe@email.com")


    def test_apply_extension(self):
        """
        test apply extension
        """
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


if __name__ == "__main__":
    unittest.main()
