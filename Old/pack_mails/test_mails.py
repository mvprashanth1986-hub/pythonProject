import unittest
import HtmlTestRunner

class MailTest(unittest.TestCase):
    def test_Gmail(self):
        print("Gmail")
        self.assertTrue(True)

    def test_Yahoo(self):
        print("Yahoo")
        self.assertTrue(True)

    def test_Rediff(self):
        print("Rediff")
        self.assertTrue(True)
