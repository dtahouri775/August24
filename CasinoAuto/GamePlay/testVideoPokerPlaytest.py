from CasinoAuto.GamePlay import MouseIntercepts
import unittest
import nose
import time
from CasinoAuto.Pages.BaseTestCase import BaseTestCase
from CasinoAuto.Constants import Casino_Constants
from CasinoAuto.Pages.VideoPokerPage import  VideoPokerPage

class videopokergamepagetest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(videopokergamepagetest, self).setUp()
        self.navigate_to_page(Casino_Constants['Base_URL'] + "/casino")
        self.driver.maximize_window()

    def testLoginfromLandingpageTest(self):

            sg_page_obj = VideoPokerPage(self.driver)
            ng = sg_page_obj.getgamenumber()
            if(Casino_Constants['Browser']=='edge'):#edge does not recognize number of images correctly
                ng=10

            print("Number of images in this page equals: ",ng)
            time.sleep(5)
            for i in range(1,ng-5):  # footer images are deducted (- 5)

                gname=sg_page_obj.click_loginfromlandingpage(i)
                print(gname)

                sg_page_obj.logout()
                time.sleep(5);
                print("i= ", i)


    def tearDown(self):
        super(videopokergamepagetest, self).tearDown()


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