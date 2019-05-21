'''
Created on April 30 , 2019

@author: Daryoush
'''
import unittest
import nose
import time
from AdminAuto.Pages.BaseTestCase import BaseTestCase
from AdminAuto.Constants import Admin_Constants
from AdminAuto.Pages.RegisterUsersPages import RegisterUserPages
class createusertest(BaseTestCase,unittest.TestCase):


    def setUp(self):
        super(createusertest, self).setUp()
        self.navigate_to_page(Admin_Constants['Client_URL'])
        self.driver.maximize_window()
        print("Access to dev06 client was successful")
    def testcreateusers(self):
        username = ""
        email = ""
        password = "Password1"
        element = RegisterUserPages(self.driver)
        for c in range(1, 7):  # 1:usd  2:eur  3:gbp 4:cad 5:aud 6:hkd
            for u in range(5, 8):#number of users
                #if(c<3 ):
                 #   continue
                if(c==1):
                    username = "mysqlb" +"usd"+str(u)
                email = username+"@yahoo.com"
                if (c == 2):
                    username = "mysqlb" + "eur"+str(u)
                if (c == 3):
                    username = "mysqlb" + "gbp"+str(u)
                if (c == 4):
                    username = "mysqlb" + "cad"+str(u)
                if (c == 5):
                    username = "mysqlb" + "aud"+str(u)
                if (c == 6):
                    username = "mysqlb" + "hkd"+str(u)

                email = username + "@yahoo.com"
                element.register(c,username,email,password)
                time.sleep(3)
                self.navigate_to_page("https://dev06.xcl.ie/casino/play/PL49/T0012?limit=0")#user will appeare in dev06
                time.sleep(3)
                print("User Created: "+username)
                element.logout()


    def tearDown(self):
            super(createusertest, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()