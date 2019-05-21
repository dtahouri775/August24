'''
Created on November 7, 2018

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


    def testusodds_backs_test(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("eur")
        backnumber = "10"
        stakenumber = "11"
        time.sleep(1)
        sg_page_obj.submit_request_malay_backoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "99"):
             print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"

        backnumber = "15"
        sg_page_obj.editbackvaluebackoffer(backnumber)
        time.sleep(1)

        profit = sg_page_obj.getprofit()

        if (profit == "150"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)

    def testusodds_BackandStake_test(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("eur")
        backnumber = "10"
        stakenumber = "11"
        time.sleep(1)
        sg_page_obj.submit_request_hkd_backoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "110"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"
        backnumber = "20"
        stakenumber = "15"
        sg_page_obj.editbackandStakevaluebackoffer(backnumber,stakenumber)
        time.sleep(1)

        profit = sg_page_obj.getprofit()

        if (profit == "285"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)

    def testsubmitwin_lose_offer_match(self):


            sg_page_obj = MainPage(self.driver)
            sg_page_obj.click_logintop_button("eur_match0")#make bet on win
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            time.sleep(1)
            backnumber = ".4"
            stakenumber = "5"
            sg_page_obj. submit_request_winoffer_match(backnumber,stakenumber,2)#2 for hkd
            time.sleep(1)
            sg_page_obj.logout()
            time.sleep(1)
            #second user will match 25% of match

            sg_page_obj.click_logintop_button("eur_match1")  # make bet on lose
            # cancell all unmatched from pervious tests so this test to be independent and clear for the scope of this test
            sg_page_obj.cancel_unmatched()
            backnumber = "2"
            stakenumber = "4"
            time.sleep(4)
            sg_page_obj.submit_request_loseoffer_match(backnumber,stakenumber)
            time.sleep(2)
            sg_page_obj.logout()

    def tearDown(self):
        # time.sleep(20)
        super(popularpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()