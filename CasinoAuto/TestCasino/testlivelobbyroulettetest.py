'''
Created on December 11, 2018
Change on December 22, 2018
@author: Daryoush
'''
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
#from CasinoAuto.Pages.LiveCasinoPage import LiveCasinoPageM
from CasinoAuto.Pages.LiveRoulettePage  import LiveroulettePage

class liveroulettetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(liveroulettetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def testLogindirectlyTest(self):

            lg_page_obj = LiveroulettePage(self.driver)
            lg_page_obj.liveroulette()
            ng = lg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            print("Info Number of images in this page equals: ng=",ng)
            time.sleep(5)
            k=0
            for i in range(1, ng - 10):  # footer images are deducted (- 5), and there are additional image on this page too
                print('Info i= ',i)
                exist=lg_page_obj.existgameimage(i)
                if(exist==1):
                    gname=lg_page_obj.click_loginfromlandingpage(i)
                    print("Info: gname=",gname)
                    lg_page_obj.logout()
                    time.sleep(5)
                if (exist == 0):
                    print("Info GameImage Does not exist:  i=",i)
                    k=k+1



    def testLandingpageGame_name_provider_Rules_DescriptionTest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info Number of images in this page equals: ng=", ng)
        time.sleep(5)
        for i in range(1, ng-10):  # footer images are deducted (- 5), and there are additional image on this page too
            #if(i!=6 and i!=9 and i!=12 and i!=15 and i!=18 and i!=21 ):#will remove once it is clrified about gray bet slip
             gname = rg_page_obj.verifylandingpageinfo(i)
             print("Info verify landing page i= ", i)
    #verifyproviderlog
    def testverifylogtest(self):
        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info Number of images in this page equals: ng=", ng)
        time.sleep(5)
        for i in range(1, ng-10):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifyproviderlog(i)
            print("Info existing log of i= ", i)
            # verifyproviderlog

    def testverifyexistingofgamename(self):

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Info Number of images in this page equals: ng=", ng)
        time.sleep(5)
        for i in range(1, ng - 6):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifygamename(i)
            print("Info game existing of i= ", i)
    def testverifyexistingofdelaername(self):

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Number of images in this page equals: ", ng)
        time.sleep(5)
        for i in range(1, ng - 6):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifydealername(i)
            if(gname==1):
                print("Info Dealer name existing of i= ", i)
            if (gname == 0):
                print("Bug in Roulette Page Dealer name is not existing of i=", i)
    def testverifyexistingofminmax(self):

        rg_page_obj = LiveroulettePage(self.driver)
        rg_page_obj.liveroulette()
        ng = rg_page_obj.getgamenumber()
        if (Casino_Constants['Browser'] == 'edge'):  # edge does not recognize number of images correctly
            ng = 12

        print("Number of game in this page equals: ng=", ng)
        time.sleep(5)
        for i in range(1, ng - 10):  # footer images are deducted (- 5)
            gname = rg_page_obj.verifygameminmax(i)
            if(gname==1):
                print("Info Existing of min-max  i= ", i)
            if (gname == 0):
                print("Bug in Roulette page: NOt Existing of min-max  i= ", i)
    def tearDown(self):
        super(liveroulettetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()