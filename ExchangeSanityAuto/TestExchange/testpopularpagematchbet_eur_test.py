'''
Created on Sept 21, 2018

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

    def testsubmitwin_lose_offer_match_Eurouser_usd(self):#This test is going to be completed next week!

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match0")#make bet on win
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber="150"
            stakenumber = "4"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,0)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("eur_match1")  # make bet on lose
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(2)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()
    def testsubmitwin_lose_offer_match_Eurouser_malay(self):#This test is going to be completed next week!

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match0")#make bet on win
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber="2.0"
            stakenumber = "40"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,3)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("eur_match1")  # make bet on lose
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(2)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()
    def testsubmitwin_lose_offer_match_Eurouser_hkd(self):#This test is going to be completed next week!

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match0")#make bet on win
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber="2.0"
            stakenumber = "40"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,2)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("eur_match1")  # make bet on lose
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(2)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()
    def testsubmitwin_lose_offer_match_Eurouser_eur(self):

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match0")#make bet on win
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber="2.0"
            stakenumber = "40"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,1)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("eur_match1")  # make bet on lose
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber = "2.0"
            stakenumber = "40"
            time.sleep(2)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            mvalue = sg_page_obj.verifymatch()
            print("Matched value updated to :",mvalue)
            if(mvalue!= None):
                    print("Pass")
            else:
                    print("Fail Matched value is not filled: Bug  103")

            sg_page_obj.logout()


    def tearDown(self):
        time.sleep(1)
        super(popularpagematchbettest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()