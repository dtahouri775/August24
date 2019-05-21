'''
Created on Sept 17, 2018

@author: Daryoush
'''


from MatchBookLoginPage import MatchBookLoginPage
from ExchangeSanityAuto.Locators.UIMapMainpage import LogInPageMap
from ExchangeSanityAuto.Locators.UIMapMainpage import MainPageMapXpath

from ExchangeSanityAuto.Constants import Exchange_Constants

from BasePage                import BasePage
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)


#defining the casino page object here
    def  _verify_page(self):
        try:
            element = self.find_element("cssSelector", MainPageMapXpath['AcceptCookiesButton'])
            element.click()
        except:
            raise Exception("Accept Cookies did not display")


        try:

            self.main = self.wait_for_element_visibility(10,"cssSelector",LogInPageMap["LoginButtonTopcssSelector"])

        except:
            raise Exception("maingameLocator is not accessable")


    def click_logintop_button(self,currency):
        temp = "CAsino_Username_" + currency
        self.click(10,
                   "cssSelector",
                   LogInPageMap['LoginButtonTopcssSelector'])
        mainWindowHandle = self.driver.window_handles
        self.click(10,
                   "xpath",
                   LogInPageMap['LogInToMatchbookTextXpath']
                   )
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
            if handle != mainWindowHandle[0]:
                self.switch_to_window(handle)
                break

        log_obj = MatchBookLoginPage(self.driver,
                                     Exchange_Constants[temp],
                                     Exchange_Constants['Casino_Password']
                                 )
        log_obj.login()
        try:
            time.sleep(2)#wait untill user name appears
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["rhsaccount"])
            element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
            element.click()
            time.sleep(2)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])
            element =  self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
            text1 = element.get_attribute('innerText')
            print(text1)

        except:
            raise Exception(" user name is not displayed")

    def submit_request_backoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)
        #Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)
        #dt
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath['rhsaccount'])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLay'],
                            backvalue
        )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self
    #testing different odds type
    def submit_request_decimal_backoffer(self, backvalue, stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)


        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self

    def submit_request_malay_backoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsMalay'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsMalay'])
        element.click()
        time.sleep(1)

        #DisplayOddsHkdXpath1
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
        )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self
    def submit_request_usd_backoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsUsd'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsUsd'])
        element.click()
        time.sleep(1)


        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
        )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self

    def submit_request_hkd_backoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsHkd'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsHkd'])
        element.click()
        time.sleep(1)

        #DisplayOddsHkdXpath1
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
        )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self
    def submit_request_hkd_backoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsHkd'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsHkd'])
        element.click()
        time.sleep(1)

        #DisplayOddsHkdXpath1
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text == "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        # end of may modify
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
        )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
        return self

    def getprofit(self):

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
        element = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
        element.click()


        time.sleep(1)
        try:
             self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipProfit'])
             element = self.find_element("cssSelector", MainPageMapXpath['BetSlipProfit'])
        except:
            try:#incase it is matched already
                self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Matchedmenu'])
                element = self.find_element("cssSelector", MainPageMapXpath['Matchedmenu'])
                element.click()
                self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipProfitmatched'])
                element = self.find_element("cssSelector", MainPageMapXpath['BetSlipProfitmatched'])
            except:
                print("BetSlipProfit is not found")


        return (element.get_attribute('value'))

    def editbackvaluebackoffer(self,backvalue):

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipBack'])
        element = self.find_element("cssSelector", MainPageMapXpath['BetSlipBack'])
        #element.click()
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )

        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)
    def editbackandStakevaluebackoffer(self,backvalue,stakevalue):

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipBack'])
        element = self.find_element("cssSelector", MainPageMapXpath['BetSlipBack'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLayStake'])
        element = self.find_element("cssSelector", MainPageMapXpath['BetSlipLayStake'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )

        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)

    def editlayoddslayoffer(self,cr,stakenumber):
        if(cr==1):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipadd'])
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipadd'])
            self.fill_out_field("cssSelector", MainPageMapXpath['BetSlipLayStake'], stakenumber)
        if (cr == 2):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipdeduct'])
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipdeduct'])
            element.click()
        if (cr == 3):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipdeduct'])
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipdeduct'])
            element.click()
            time.sleep(2)
            self.fill_out_field("cssSelector", MainPageMapXpath['BetSlipLayStake'],stakenumber )



        time.sleep(2)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)



    def cancel_unmatched(self):
        try:

            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DeleteButtonUnmatched'])

            element = self.find_element("cssSelector", MainPageMapXpath['DeleteButtonUnmatched'])
            element.click()
            time.sleep(2)
        except:
            print("No need to cancel")





    def returnofferamount(self):#one for back offer, 2 for layoffer
        try:
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['UpdatedOffervaluelay'])

            element3 = self.find_element("cssSelector", MainPageMapXpath['UpdatedOffervaluelay'])
        except:#need to think find the discreqpeny
           print("UpdatedOffervalue is not visible")
        text1 = element3.get_attribute('innerText')
        return text1
    def returnavailablebalance(self):
        try:

            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Availablebalance'])

            element3 = self.find_element("cssSelector", MainPageMapXpath['Availablebalance'])
        except:#
            print("Available balance is not available Bug :101")

        text1 = element3.get_attribute('innerText')
        return text1

    def returnloseofferamount(self):
        try:
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['UpdatedOffervaluewin'])

            element3 = self.find_element("cssSelector", MainPageMapXpath['UpdatedOffervaluewin'])
        except:
            print("UpdatedOffervaluewin is not there!")
        text1 = element3.get_attribute('innerText')
        return text1

    def logout(self):
        time.sleep(5)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["rhsaccount"])

        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["logout"])
        element2 = self.find_element("cssSelector", MainPageMapXpath["logout"])
        element2.click()
        time.sleep(2)
    def submit_request_laybet(self,backvalue,stakevalue):
       #may modify this portion
       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])

       element = self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
       element.click()
       time.sleep(3)

       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
       element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
       element.click()
       time.sleep(1)
       # Decimal selection
       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
       element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
       element.click()
       time.sleep(1)
       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
       element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
       element.click()
       time.sleep(1)
       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
       element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
       text = element.get_attribute('innerText')
       if (text == "Binary"):  # should be switched to binary to be valid for this option
           element.click()
       time.sleep(1)

       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
       element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
       element.click()
       time.sleep(1)
       # end of may modify
       element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
       element.click()
       time.sleep(3)

       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2LayMakeOffer'])

       element = self.find_element("cssSelector", MainPageMapXpath['sec2LayMakeOffer'])
       element.click()
       time.sleep(1)
       self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLay'],
                            backvalue
        )
       self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
       time.sleep(1)
       self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])

       element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
       element3.click()
       time.sleep(1)
       #Place Bet
       return self
#
    def submit_request_winoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])

        element = self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)
        # Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if(text == "Back-Lay"):#should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['HorseRaceWin4'])
        element = self.find_element("cssSelector", MainPageMapXpath['HorseRaceWin4'])
        element.click()
        #element.click()
        time.sleep(1)

        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS1W'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS1S'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS1Check'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BS1Check'])
        element3.click()
        time.sleep(1)
        return self
    def submit_edit_request_winoffer(self,cr,backvalue,stakevalue):

        if (cr == 1):  # edit both odds and  Stake value of win offer
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
            element.click()
            time.sleep(1)
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipBack'],
                                backvalue
                                )
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipLayStake'],
                                stakevalue
                                )

            time.sleep(1)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3.click()
            time.sleep(1)
        if(cr==2):#edit odd value of win offer
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
            element.click()
            time.sleep(1)
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipBack'],
                                backvalue
                                )

            time.sleep(1)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3.click()
            time.sleep(1)
        if (cr == 3):  # edit stak value of win offer
            element = self.find_element("cssSelector", MainPageMapXpath['BS1W'])
            element.click()
            time.sleep(1)
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BS1W'],
                                stakevalue
                                )
            time.sleep(1)
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipProfit'])
            element.click()
            time.sleep(1)

            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS1Check'])

            element3 = self.find_element("cssSelector", MainPageMapXpath['BS1Check'])
            element3.click()
            time.sleep(1)
        return self
    def submit_request_winoffer_match(self,backvalue,stakevalue,oddstype):#oddstype 0 :US 1:DECIMAL 2:HK 3:MALAY
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])

        element = self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(2)
        # Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)
        if (oddstype == 0):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsUsd'])
            element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsUsd'])
            element.click()
            time.sleep(1)
        if (oddstype == 1):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
            element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
            element.click()
            time.sleep(1)
        if(oddstype == 2):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsHkd'])
            element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsHkd'])
            element.click()
            time.sleep(1)
        if (oddstype == 3):
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsMalay'])
            element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsMalay'])
            element.click()
            time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if(text == "Back-Lay"):#should be switched to binary to be valid for this option
            element.click()
        time.sleep(2)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(2)
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)
        try:
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['SelectMatchwon'])
            element = self.find_element("cssSelector", MainPageMapXpath['SelectMatchwon'])
            element.click()

        except:
			print("Bug: SelectMatchwon is not available")
        
        time.sleep(2)

        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(2)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
        element3.click()
        time.sleep(3)
        return self
    def submit_request_loseoffer_match(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])

        element = self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(2)
        # Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if(text == "Back-Lay"):#should be switched to binary to be valid for this option
            element.click()
        time.sleep(4)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(2)
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)
        try:
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['SelectMatchLose'])
            element = self.find_element("cssSelector", MainPageMapXpath['SelectMatchLose'])
            element.click()
            time.sleep(2)
        except:#just in case win bet is empty box we try this!
            print("Bug  on match lose")



        self.fill_out_field("cssSelector",
        MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(2)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
        element3.click()
        time.sleep(3)
        return self


    def submit_request_loseoffer(self,backvalue,stakevalue):
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath["Usernametitle"])

        element = self.find_element("cssSelector", MainPageMapXpath["Usernametitle"])
        element.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)
        # Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        time.sleep(1)
        element.click()
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if(text == "Back-Lay"):#should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        element = self.find_element("cssSelector", MainPageMapXpath["rhsaccount"])
        element.click()
        time.sleep(3)
        try:#depends on how many has been filled in the past
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['SelectMatchLose'])
            element = self.find_element("cssSelector", MainPageMapXpath['SelectMatchLose'])
            element.click()
        except:
            print("Bug: Horse racing first spot lose offer is not displayed")

        #element.click()
        time.sleep(1)

        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
        element3.click()
        time.sleep(1)

        return self
    def submit_edit_request_loseoffer(self,cr,backvalue,stakevalue):

        if (cr == 1):  # edit both back value of lose offer
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipadd'])
            element.click()
            time.sleep(2)

            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipBack'],
                                backvalue
                                )
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipLayStake'],
                                stakevalue
                                )

            time.sleep(1)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3.click()
            time.sleep(2)
        if(cr==2):#edit back value of lose offer
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
            element.click()
            time.sleep(2)
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipBack'],
                                backvalue
                                )

            time.sleep(1)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3.click()
            time.sleep(2)
        if (cr == 3):  # edit stak value of lose offer
            element = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
            element.click()
            time.sleep(2)
            self.fill_out_field("cssSelector",
                                MainPageMapXpath['BetSlipLayStake'],
                                stakevalue
                                )
            time.sleep(2)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])

            element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipLaycheckmark'])
            element3.click()
            time.sleep(1)
        return self
    def deposit(self):
        try:
            time.sleep(1)
            self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DepositDilagbox'])
            element3 = self.find_element("cssSelector", MainPageMapXpath['DepositDilagbox'])
            element3.click()
            return "1";
        except:
            raise Exception("Bug: deposit")
            return "0"

    def submitbetuserlogout(self,backvalue, stakevalue):

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['sec2BackMakeOffer'])

        element = self.find_element("cssSelector", MainPageMapXpath['sec2BackMakeOffer'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backvalue
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakevalue
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['ReviewOrderPlaceBet'])

        element = self.find_element("cssSelector", MainPageMapXpath['ReviewOrderPlaceBet'])
        element.click()
        time.sleep(1)

        try:
            time.sleep(1)
            mainWindowHandle = self.driver.window_handles
            self.click(10,
                       "xpath",
                       LogInPageMap['LogInToMatchbookTextXpath']
                       )
            return "1";
        except:
            print("Bug: in LogInToMatchbookTextXpath ")
            return "0"


    def submit_multiple_offer(self,backnumber_w3, stakenumber_w3, backnumber_w4, stakenumber_w4, backnumber_l5, stakenumber_l5, backnumber_d3, stakenumber_d3):

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Usernametitle'])

        element = self.find_element("cssSelector", MainPageMapXpath['Usernametitle'])
        element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplaySettingPopup'])
        element.click()
        time.sleep(1)
        # Decimal selection
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsArrow'])
        element.click()
        time.sleep(1)
        # dt
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayOddsDecimal'])
        element.click()
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeTypecheckbox'])
        text = element.get_attribute('innerText')
        if (text != "Binary"):  # should be switched to binary to be valid for this option
            element.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element = self.find_element("cssSelector", MainPageMapXpath['DisplayDetailExchangeUpdate'])
        element.click()
        time.sleep(1)
        '''
        After recent change in the right bar we do not need these at all
        # end of may modify
        element = self.find_element("xpath", MainPageMapXpath['UserRightTopnameXpath1'])
        element.click()
        time.sleep(6)#The delay time must be enough so bet completely submitted
        '''
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['HorseRaceWin3'])

        element = self.find_element("cssSelector", MainPageMapXpath['HorseRaceWin3'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backnumber_w3
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakenumber_w3
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(6)
        #second bet
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['HorseRaceWin4'])

        element = self.find_element("cssSelector", MainPageMapXpath['HorseRaceWin4'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backnumber_w4
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakenumber_w4
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(6)
        #thirdbet
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['HorseRaceLose5'])

        element = self.find_element("cssSelector", MainPageMapXpath['HorseRaceLose5'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backnumber_l5
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakenumber_l5
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(6)

        #fourth bet

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['AvsTDrawWin3'])

        element = self.find_element("cssSelector", MainPageMapXpath['AvsTDrawWin3'])
        element.click()
        time.sleep(1)
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipBack'],
                            backnumber_d3
                            )
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BetSlipLayStake'],
                            stakenumber_d3
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipcheckmark'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipcheckmark'])
        element3.click()
        time.sleep(3)



    def edit_multiple_offer(self,backnumber_w3, stakenumber_w3, backnumber_w4, stakenumber_w4, backnumber_l5, stakenumber_l5, backnumber_d3, stakenumber_d3):

        #click unmatched to edit
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BetSlipunmatchedmenu'])
        element3.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS1W'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS1W'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS1W'],
                            backnumber_w3
                            )
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS1S'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS1S'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS1S'],
                            stakenumber_w3
                            )

        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS1Check'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BS1Check'])
        element3.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS2W'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS2W'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS2W'],
                            backnumber_w4
                            )
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS2S'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS2S'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS2S'],
                            stakenumber_w4
                            )

        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS2Check'])

        element3 = self.find_element("cssSelector", MainPageMapXpath['BS2Check'])
        element3.click()
        time.sleep(3)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS3W'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS3W'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS3W'],
                            backnumber_l5
                            )
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS3S'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS3S'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS3S'],
                            stakenumber_l5
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS3Check'])
        element3 = self.find_element("cssSelector", MainPageMapXpath['BS3Check'])
        element3.click()
        time.sleep(3)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS4W'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS4W'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS4W'],
                            backnumber_d3
                            )
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS4S'])
        element = self.find_element("cssSelector", MainPageMapXpath['BS4S'])
        self.fill_out_field("cssSelector",
                            MainPageMapXpath['BS4S'],
                            stakenumber_d3
                            )
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['BS4Check'])
        element3 = self.find_element("cssSelector", MainPageMapXpath['BS4Check'])
        element3.click()
        time.sleep(3)

    def verifymatch(self):
        time.sleep(1)
        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['Matchedmenu'])
        element3 = self.find_element("cssSelector", MainPageMapXpath['Matchedmenu'])
        element3.click()
        time.sleep(1)

        self.wait_for_element_visibility(10, "cssSelector", MainPageMapXpath['MatchedTotAmount'])
        element3 = self.find_element("cssSelector", MainPageMapXpath['MatchedTotAmount'])
        element3.click()
        #temp = element3.get_attribute('value')#should return None
        temp = element3.text
        return (temp)

    def nothanks(self):#some times it appears causes bug, in matchoffer
        try:
            element3 = self.find_element("cssSelector", MainPageMapXpath["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"




