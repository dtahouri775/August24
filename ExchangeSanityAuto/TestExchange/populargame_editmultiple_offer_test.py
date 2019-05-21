'''
Created on November 14, 2018

@author: Daryoush
'''
import unittest
import nose
import time
from ExchangeSanityAuto.Basetestcase import BaseTestCase
#from ExchangeSanityAuto.Constants import Exchange_Constants
from ExchangeSanityAuto.Pages.MainPage import MainPage
from ExchangeSanityAuto.Constants import Exchange_Constants

class popularpagetest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(popularpagetest, self).setUp()
        self.navigate_to_page(Exchange_Constants['Base_URL'] )
        self.driver.maximize_window()


    def testsubmitEdit_multiple_offer_Eur(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("eur")
        #entry numbers
        backnumber_w3 = "1.5"
        stakenumber_w3 = "10"
        backnumber_w4 = "2.5"
        stakenumber_w4 = "11"
        backnumber_l5 = "3.2"
        stakenumber_l5 = "7"
        backnumber_d3 = "4.5"#d:draw
        stakenumber_d3 = "7"



        time.sleep(1)
        sg_page_obj.submit_multiple_offer(backnumber_w3, stakenumber_w3, backnumber_w4, stakenumber_w4, backnumber_l5, stakenumber_l5, backnumber_d3, stakenumber_d3)
        time.sleep(1)

        # edited numbers
        backnumber_w3 = "3.5"
        stakenumber_w3 = "13"
        backnumber_w4 = "5.3"
        stakenumber_w4 = "8"
        backnumber_l5 = "1.25"
        stakenumber_l5 = "7"
        backnumber_d3 = "1.5"  # d:draw
        stakenumber_d3 = "3"

        sg_page_obj.edit_multiple_offer(backnumber_w3, stakenumber_w3, backnumber_w4, stakenumber_w4, backnumber_l5,
                                          stakenumber_l5, backnumber_d3, stakenumber_d3)
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)

    def tearDown(self):
        # time.sleep(20)
        super(popularpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()