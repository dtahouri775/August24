'''
Created on Aug 14, 2018

@author: Daryoush
'''
#from selenium import webdriver
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.CasinoPage import CasinoPage

class casinotabstest(BaseTestCase,unittest.TestCase):


    def setUp(self):
        super(casinotabstest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL']+"/casino")
        self.driver.maximize_window()
        
    #Verify New games link is available
    def testNewGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.newgames()
        #time.sleep(2)
    #Verify A User Can Access "Popular Games" in Casino
    def testPopularGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.populargames()
        #time.sleep(2)   
    #Verify A User Can Access Jackpots In Casino
    def testJackPotGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.jackpotgames()
    #Verify A User Can Access Slots in Casino
    def testSlotsGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.slotgames()
        #time.sleep(2)       #time.sleep(2)
    #Verify A User Can Access Table Games in Casino
    def testTableGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.tablegames()
        #time.sleep(2)this is only for the test
    #Verify A User Can Access Video Poker in Casino
    def testVideoPokerGamesTabsTest(self):
        casino_page_obj = CasinoPage(self.driver)
        casino_page_obj.videopokergames()
        time.sleep(2)  
   
    def tearDown(self):
        super(casinotabstest, self).tearDown()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    nose.main()