'''
Created on October 9, 2018

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


    def testsubmitEdit_BackOdds_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "1.892"
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "8.93"):
             print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"

        backnumber = "1.925"
        sg_page_obj.editbackvaluebackoffer(backnumber)
        time.sleep(1)

        profit = sg_page_obj.getprofit()

        if (profit == "9.26"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)
    def testsubmitEdit_BackOddsStake_offer_aud(self):
        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "1.892"
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(backnumber, stakenumber)

        profit = sg_page_obj.getprofit()

        if (profit == "8.93"):
             print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"

        newbacknumber = "1.925"
        newstakenumber = "20"
        sg_page_obj.editbackandStakevaluebackoffer(newbacknumber,newstakenumber)
        time.sleep(1)

        newprofit = sg_page_obj.getprofit()

        if (newprofit != profit):
            print("The newprofit bet profit=:", newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)

    def testsubmitEdit_BackStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        oddsnumber = "1.892"
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_backoffer(oddsnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "8.93"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"


        newstakenumber = "20"
        sg_page_obj.editbackandStakevaluebackoffer(oddsnumber, newstakenumber)
        time.sleep(1)

        newprofit = sg_page_obj.getprofit()

        if (newprofit != profit):
            print("The newprofit bet profit=:", newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)

    def testsubmitEdit_LayOdds_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        laynumber = "1.885"#ask question from Cathal for auto correction to 1.884
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_laybet(laynumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "8.85"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print" The Calculation of profit may not be correct"
        time.sleep(3)

        laynumber = "1.892"#only + sing works? ask question from Cathal
        newstakenumber = "12"
        sg_page_obj.editlayoddslayoffer(1, newstakenumber)  # 1 means adding, 2 means deductin, 3 means edit both lay and stake
        time.sleep(1)

        profit = sg_page_obj.getprofit()

        if (profit == "8.93"):
            print("The updated bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The edit value of profit may not be correct"

        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)
    def testsubmitEdit_LayStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        laynumber = "1.885"  # ask question from Cathal for auto correction to 1.884
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_laybet(laynumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "8.85"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit is not correct"
        time.sleep(3)


        newstakenumber = "20"
        sg_page_obj.editlayoddslayoffer(1,
                                         newstakenumber)  # 1 means adding, 2 means deductin, 3 means edit both lay and stake
        time.sleep(1)

        newprofit = sg_page_obj.getprofit()
        #newprofit=17.54
        if (newprofit !=  profit):
            print("The new profit is: ",newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when both stake and lay are edited"

        time.sleep(1)


    def testsubmitEdit_LayOddsStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        laynumber = "1.885"  # ask question from Cathal for auto correction to 1.884
        stakenumber = "10"
        time.sleep(1)
        sg_page_obj.submit_request_laybet(laynumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()

        if (profit == "8.85"):
            print("The initial bet profit=:", profit)  # shows current profit
        else:
            print"Fail: The Calculation of profit may or may not be correct"
        time.sleep(3)

        laynumber = "1.892"  # only + sing works? ask question from Cathal
        newstakenumber = "20"
        sg_page_obj.editlayoddslayoffer(3,
                                         newstakenumber)  # 1 means changing stake, 2 means deducting odds, 3 means edit both lay and stake
        time.sleep(1)

        newprofit = sg_page_obj.getprofit()
        #newprofit=17.54
        if (newprofit !=  profit):
            print(newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when both stake and lay are edited"

        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()
        time.sleep(1)
    def testsubmitEdit_WinOdds_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_winoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print(profit)
        time.sleep(1)

        newbacknumber = "7.0"
        time.sleep(1)
        sg_page_obj.submit_edit_request_winoffer(2,newbacknumber, stakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit !=  profit):
            print("The newprofit is :",newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when backnumber is edited"
        time.sleep(1)
            # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitEdit_WinStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_winoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print("initial value of profit is ",profit)
        time.sleep(1)

        newstakenumber = "5.37"
        time.sleep(1)
        sg_page_obj.submit_edit_request_winoffer(3, backnumber, newstakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit != profit):
            print("new profit is: ",newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when stak number is edited"
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitEdit_WinOddsStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        odds = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_winoffer(odds, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print(profit)
        time.sleep(1)

        newstakenumber = "5.37"
        newodds ="2"
        time.sleep(1)
        sg_page_obj.submit_edit_request_winoffer(1, newodds, newstakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit != profit):
            print("the new profit value is: ",newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when stak number is edited"
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitEdit_LoseStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        backnumber = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_loseoffer(backnumber, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print(profit)
        time.sleep(1)

        newstakenumber = "5.37"
        time.sleep(1)
        sg_page_obj.submit_edit_request_loseoffer(3,backnumber, newstakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit != profit):
            print(newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when stak number is edited"
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitEdit_LoseOdds_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        odds = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_loseoffer(odds, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print("The value of profit is :",profit)
        time.sleep(1)

        newsodds= "2"
        time.sleep(1)
        sg_page_obj.submit_edit_request_loseoffer(2,newsodds,stakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit != profit):
            print("New profit value is: ",newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when stak number is edited"
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def testsubmitEdit_LoseOddsStake_offer_aud(self):

        sg_page_obj = MainPage(self.driver)
        sg_page_obj.click_logintop_button("aud")
        odds = "5.0"
        stakenumber = "4.26"
        time.sleep(1)
        sg_page_obj.submit_request_loseoffer(odds, stakenumber)
        time.sleep(1)
        profit = sg_page_obj.getprofit()
        print("intital profit =",profit)
        time.sleep(1)

        newsodds = "2"
        stakenumber="6.26"
        time.sleep(1)
        sg_page_obj.submit_edit_request_loseoffer(1, newsodds, stakenumber)
        time.sleep(1)
        newprofit = sg_page_obj.getprofit()
        if (newprofit != profit):
            print(newprofit)  # shows current profit
        else:
            print"Fail: The edit value of profit is not correct when stak number is edited"
        time.sleep(1)
        # Cancel the bet slip
        sg_page_obj.cancel_unmatched()

    def tearDown(self):
        # time.sleep(20)
        super(popularpagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()