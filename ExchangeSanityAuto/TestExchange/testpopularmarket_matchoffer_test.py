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

class popularpagematchbettest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(popularpagematchbettest, self).setUp()
        self.navigate_to_page(Exchange_Constants['Base_URL'] )
        self.driver.maximize_window()

    def testsubmitwin_lose_offer_match_Eurouser(self):

            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match2")#make bet on win
            backnumber="2.0"
            stakenumber = "40"
            time.sleep(1)
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,1)
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(2)
            sg_page_obj.nothanks()  # In case No thanks button appear
            #second user will match 25% of match but differenc currency so should not increase really 25%

            sg_page_obj.click_logintop_button("gbp1_match1")  # make bet on lose
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()
            time.sleep(2)
            sg_page_obj.nothanks()  # In case No thanks button appear
            # Third user will match 25% of match  but differenc currency so should not increase really 25%

            sg_page_obj.click_logintop_button("aud1_match1")  # make bet on lose  but differenc currency so should not increase really 25%
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()
            time.sleep(2)
            sg_page_obj.nothanks()  # In case No thanks button appear
            sg_page_obj.click_logintop_button("cad1_match1")  # make bet on lose  but differenc currency so should not increase really 25%
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            #creteria for pass/fail
            sg_page_obj.logout()
            time.sleep(1)
            sg_page_obj.nothanks()  # In case No thanks button appear

            sg_page_obj.click_logintop_button("hkd1_match1")  # make bet on lose  but differenc currency so should not increase really 25%
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber, stakenumber)
            time.sleep(2)
            # creteria for pass/fail
            sg_page_obj.logout()
            time.sleep(5)

            sg_page_obj.click_logintop_button("usd1_match1")  # make bet on lose  but differenc currency so should not increase really 25%
            backnumber = "2.0"
            stakenumber = "10"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber, stakenumber)
            time.sleep(2)
            # creteria for pass/fail
            sg_page_obj.logout()
            time.sleep(2)
            sg_page_obj.nothanks()#In case No thanks button appear


    def tearDown(self):
        time.sleep(1)
        super(popularpagematchbettest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()