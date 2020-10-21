import unittest
import HtmlTestRunner

from Old.pack_mails.test_mails import MailTest              #Import all files from all packages
from Old.pack_wallets import LoginTest
from Old.pack_wallets.test_wallets import Wallets

mails=unittest.TestLoader().loadTestsFromTestCase(MailTest)         #Load all test methods
login=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
wallets=unittest.TestLoader().loadTestsFromTestCase(Wallets)

Sanity = unittest.TestSuite([mails,login])                          #Create Testsuits
Functional = unittest.TestSuite([mails,login,wallets])

unittest.TextTestRunner(verbosity=2).run(Functional)               #Run Testsuits

if __name__ == "__main__":
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\pythonutils\Reports'))