'''
Created on November 13, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from ExchangeSanityAuto.BaseTestCase import BaseTestCase
from ExchangeSanityAuto.Constants import Exchange_Constants
from ExchangeSanityAuto.Pages.MainPage import MainPage
from ExchangeSanityAuto.Constants import Exchange_Constants

class popularpagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(popularpagetest, self).setUp()
        self.navigate_to_page(Exchange_Constants['Base_URL'] )
        self.driver.maximize_window()


        # Verify user can access from each game landing page
    def submit_offer_when_user_is_logged_out_test(self):

        sg_page_obj = MainPage(self.driver)
        backnumber="5.0"
        stakenumber="2"
        time.sleep(1)
        testresult=sg_page_obj.submitbetuserlogout(backnumber,stakenumber)
        time.sleep(1)

        if( testresult=="1"):
            print("Pass: Deposit box opend for adding funds")
        else:
            print("Fail the test More than Balance!!")






        #Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def tearDown(self):
        # time.sleep(20)
        super(popularpagetest, self).tearDown()

    if __name__ == "__main__":
        # unittest.main()
        nose.main()

