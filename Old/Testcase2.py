import unittest
from selenium import webdriver


def setUpModule():
    print("module begins")

def tearDownModule():
    print("Module ends")

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class starts")

    @classmethod
    def tearDownClass(cls):
        print("class ends")

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    @unittest.skip("Skipping google")
    def test_google(self):
        print("Google")

    def test_yahoo(self):
        print("Yahoo")

    @unittest.SkipTest
    def test_facebook(self):
        print("facebook")

    @unittest.skipIf(1==1, "one equal one")
    def test_instagram(self):
        print("instagram")

if __name__ == "__main__":
    unittest.main()