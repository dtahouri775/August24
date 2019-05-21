'''
Created on Aug 14, 2018

@author: Daryoush
'''

from CasinoAuto.Locators.UIMapCasinoPage import  CasinoPageMapXpath
from CasinoAuto.Locators.UIMapCasinoPage import  SearchResult
from CasinoAuto.Locators.UIMapCasinoPage import  LogInPageMap
from CasinoAuto.Constants                                import Casino_Constants
from MatchBookLoginPage import MatchBookLoginPage
from BasePage                import BasePage
from CasinoAuto.Locators.UIMapHomePage import HomePageMapXpath
import time
class CasinoPage(BasePage):
    def __init__(self, driver):
        super(CasinoPage, self).__init__(driver)
        #self.nhl = self.driver.find_element(CasinoPageMapXpath["lhncasinoLocatorXpath"])
        #self.nhl.click()
        #self.driver.navigate_to_page("https://dev06.xcl.ie/casino")
        
#defining the casino page object here
    def  _verify_page(self):
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["newgameLocator"]  )
        except:   
            raise Exception("newgameLocator is not accessable")
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["popularLocator"]  )
        except:   
            raise Exception("popularLocator is not accessable")
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["jackpotsLcoator"]  )
        except:   
            raise Exception("jackpotsLcoator is not accessable")
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["slotgameLcoator"]  )
        except:   
            raise Exception("slotgame is not accessable")

        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["tablegametablocator"]  )
        except:   
            raise Exception("tablegametablocator is not accessable")
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["videopokerlocator"]  )
        except:   
            raise Exception("videopokerlocator is not accessable")
        try:
            
            self.wait_for_element_visibility(10,"cssSelector",CasinoPageMapXpath["searchcasinoLocator"]  )
        except:   
            raise Exception("searchcasinolocator is not accessable")
        try:

            self.wait_for_element_visibility(10, "cssSelector", LogInPageMap["LoginButtonTop"])
        except:
            raise Exception("LogInPageMap is not accessable")
        
    def newgames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["newgameLocator"]
        )
        
    def populargames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["popularLocator"]
        )    
    def jackpotgames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["jackpotsLcoator"]
        )
        
    def slotgames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["slotgameLcoator"]
        )        
    def tablegames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["tablegametablocator"]
        )
    def videopokergames(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["videopokerlocator"]
        )

    def livecasinolink(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["liveDealer"]
        )

    def searchcasinolink(self):
        self.click(10, 
                   "cssSelector",
                   CasinoPageMapXpath["searchcasinoLocator"]
        ) 
    def submit_request_search(self,testitem):
        self.fill_out_field("cssSelector",
                            CasinoPageMapXpath['searchcasinoLocator'],
                            testitem
        )
        return self    
    def verifygamExisting(self,testitem2):
        try:
            self.find_element("cssSelector", SearchResult[testitem2])
        except:
            raise Exception(testitem2 +" is not displayed")

    def click_logintop_button(self):
        self.click(10,
                   "cssSelector",
                   LogInPageMap['LoginButtonTop'])
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
                                  Casino_Constants['CAsino_Username'],
                                  Casino_Constants['Casino_Password']
                                 )
        log_obj.login()
        try:
            self.wait_for_element_visibility(10, "cssSelector", HomePageMapXpath["rhsaccount"])
            element = self.find_element("cssSelector", HomePageMapXpath["rhsaccount"])
            element.click()
            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["Usernametitle"])
            element =  self.find_element("cssSelector", CasinoPageMapXpath["Usernametitle"])
            text1 = element.get_attribute('innerText')
            print(text1)
            if(text1==Casino_Constants["CAsino_Username"]):
                print("Successful Log in")
        except:
            print(" user name is not displayed will try usernamebonus too")

        try:
            self.wait_for_element_visibility(10, "cssSelector", CasinoPageMapXpath["bonususernametitle"])
            element =  self.find_element("cssSelector", CasinoPageMapXpath["bonususernametitle"])
            text1 = element.get_attribute('innerText')
            print(text1)
            if(text1==Casino_Constants["CAsino_Username"]):
                print("Successful Log in")
        except:
            print(" user name has not assigned bonus yet")

