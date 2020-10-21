import unittest
import HtmlTestRunner

class Wallets(unittest.TestCase):
    def test_paytm(self):
        print("paytm")
        self.assertTrue(True)

    def test_googlepay(self):
        print("googlepay")
        self.assertTrue(True)

    def test_phonepay(self):
        print("phonepay")
        self.assertTrue(True)
