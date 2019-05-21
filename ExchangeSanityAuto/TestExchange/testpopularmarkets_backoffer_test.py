'''
Created on Sept 17, 2018

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
    def testsubmitbackofferEurouser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("eur")
        backnumber="5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber,stakenumber)
        time.sleep(1)
        marketvalue =  sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:3]
        testvalue = ord(displayedcurrency)
        if(testvalue==8364):
            print("Passed ",testvalue)#8364 for Euro
        else:
            print"Fail: The Euo currency is not displayed correctly"

        #Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitbackofferGbpuser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("gbp")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        marketvalue = sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:3]
        testvalue = ord(displayedcurrency)
        if (testvalue == 163):
            print(testvalue)  # 163 for GBP
        else:
            print"Fail: The Great British currency is not displayed correctly"
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def testsubmitbackofferCaduser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("cad")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        marketvalue = sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:5]
        if (displayedcurrency == "CA$"):
            print(displayedcurrency)  # CA$ for Canadian dollar
        else:
            print"Fail: The Canadian currency is not displayed correctly"
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def testsubmitbackofferAudduser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        marketvalue = sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:4]
        if (displayedcurrency == "A$"):
            print(displayedcurrency)  # CA$ for Canadian dollar
        else:
            print"Fail: The Australian currency is not displayed correctly"
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def testsubmitbackofferHkdduser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("hkd")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        marketvalue = sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:5]
        if (displayedcurrency == "HK$"):
            print(displayedcurrency)  # HK$ for Honk kong dollar
        else:
            print"Fail: The Australian currency is not displayed correctly"
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def testsubmitbackofferUsdduser(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("usd")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        marketvalue = sg_page_obj.returnofferamount()
        displayedcurrency = marketvalue[2:3]
        if (displayedcurrency == "$"):
            print(displayedcurrency)  # $ for American dollar
        else:
            print"Fail: The Australian currency is not displayed correctly"
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
    def tearDown(self):
        #time.sleep(20)
        super(popularpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()