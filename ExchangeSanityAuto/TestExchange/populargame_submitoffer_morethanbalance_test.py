'''
Created on November 13, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from ExchangeSanityAuto.Basetestcase import BaseTestCase
from ExchangeSanityAuto.Constants import Exchange_Constants
from ExchangeSanityAuto.Pages.MainPage import MainPage
from ExchangeSanityAuto.Constants import Exchange_Constants

class popularpagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(popularpagetest, self).setUp()
        self.navigate_to_page(Exchange_Constants['Base_URL'] )
        self.driver.maximize_window()


        # Verify user can access from each game landing page
    def testsubmitbackofferEurouserMorthanBalance(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("eur")
        stakenumber=sg_page_obj.returnavailablebalance()
        backnumber="5.0"

        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber,stakenumber)
        time.sleep(1)
        testresult = sg_page_obj.deposit() # will becompleted
        if( testresult=='1'):
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

