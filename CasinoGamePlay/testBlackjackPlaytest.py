import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from AdminAuto.Pages.GamePlayPage import  GamePlayPage

class tableblackjackgamepagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(tableblackjackgamepagetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()




    def testPlayBlackjackloginest(self):
        print("Under Development")
        sg_page_obj = GamePlayPage(self.driver, "dunfeur1", "Password1")
        sg_page_obj.login()
        time.sleep(5)
        sg_page_obj.acceptcookies()
        sg_page_obj.gotoblackjacklimit0()
        time.sleep(10)
        sg_page_obj.installflashgame()
        time.sleep(40)
        sg_page_obj.playbjgames(10000)


    '''
    def testUnfinishedGameLoginfromLandingpageTest(self):
            print("Under Development")
            
            sg_page_obj = TableGamesPage(self.driver)
            time.sleep(5)

            for i in range(17,111):  # footer images are deducted (- 5)
                sg_page_obj.nothanks()
                username = "dunfeur"
                username=username+str(i)
                gname = sg_page_obj.click_loginfromlandingpage2(1,username)
                time.sleep(10)
                for j in range(1,2):

                    print(gname)
                    #if(i==3):# we do not close explore one time install is enough
                    sg_page_obj.installflash()

                    time.sleep(30)
                    sg_page_obj.clickme(1230, 720)  # close release bonus
                    print("close release bonus")
                    time.sleep(5)
                    sg_page_obj.clickme(625, 1010)  # chips selected
                    print("chips selected")
                    time.sleep(2)
                    sg_page_obj.clickme(620, 760)#chips located
                    print("chips located")
                    time.sleep(2)
                    sg_page_obj.clickme(1170, 1100)  # Deal buttton Pressed
                    print("Deal button Pressed")
                    time.sleep(2)
                    #sg_page_obj.clickme(1370, 1120)  # No Insurance buttton Pressed
                    #print("No Insurance buttton Pressed")
                    sg_page_obj.nothanks()
                print("Befor Logout2")
                sg_page_obj.logout2()
                time.sleep(3)
                sg_page_obj.nothanks()
                time.sleep(5);
                print("i= ", i)
    '''

    def tearDown(self):
        super(tableblackjackgamepagetest, self).tearDown()


if __name__ == "__main__":
    # unittest.main()
    nose.main()



'''
if (x == 0) // Match book Jacks or better
{

    rb.mouseMove((int)(RobatConst.MB_x0_69 * getx()), (int)(RobatConst.MB_y0_69 * gety())); // Press
Deal
rb.delay(2000);
rb.mousePress(InputEvent.BUTTON1_MASK);
Thread.sleep(500);
rb.mouseRelease(InputEvent.BUTTON1_MASK);
System.out.println("Deal is done!");
rb.delay(8000); // Wait
to
card is dealt

rb.mousePress(InputEvent.BUTTON1_MASK);
Thread.sleep(500);
rb.mouseRelease(InputEvent.BUTTON1_MASK);
System.out.println("Draw is done!");
Thread.sleep(8000);
}
'''