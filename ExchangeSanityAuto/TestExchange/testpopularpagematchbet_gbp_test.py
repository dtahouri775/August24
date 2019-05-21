'''
Created on October 1, 2018

@author: Daryoush

'''
import unittest
import nose
import time
from ExchangeSanityAuto.BaseTestCase import BaseTestCase
from ExchangeSanityAuto.Constants import Exchange_Constants
from ExchangeSanityAuto.Pages.MainPage import MainPage
from ExchangeSanityAuto.Constants import Exchange_Constants
# This is only simple sanity type of testing, complex creteria of testing can be easily implemented
class popularpagematchbettest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(popularpagematchbettest, self).setUp()
        self.navigate_to_page(Exchange_Constants['Base_URL'] )
        self.driver.maximize_window()

    def testsubmitwin_lose_offer_match_Eurouser(self):#This test is going to be completed next week!

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("gbp2_match1")#make bet on win
            backnumber="2.0"
            stakenumber = "40"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,2)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("gbp3_match1")  # make bet on lose
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()

    def tearDown(self):
        time.sleep(1)
        super(popularpagematchbettest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()