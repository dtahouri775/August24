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
from AdminAuto.Constants import Admin_Dynamic
class createusertest(BaseTestCase,unittest.TestCase):


    def setUp(self):
        super(createusertest, self).setUp()
        self.navigate_to_page(Admin_Constants['Client_URL'])
        self.driver.maximize_window()
        print("Access to dev06 client was successful")
    def testcreateusers(self):
        if (Admin_Dynamic['createallusers'] == "1"):
            username = ""
            email = ""
            password = Admin_Dynamic['uipassword']

            element = RegisterUserPages(self.driver)
            for c in range(1, 7):  # 1:usd  2:eur  3:gbp 4:cad 5:aud 6:hkd
                for u in range(1, 8):#number of users for seven bonus types e.g. regular, Match,Freespin(Mb,NetEnt, RT), Deposit, HF

                    #if(c<6 ):
                     #   continue
                    element.nothanks()
                    if(c==1):
                        username = Admin_Dynamic['globalname'] +"usd"+str(u)
                    email = username+"@yahoo.com"
                    if (c == 2):
                        username = Admin_Dynamic['globalname'] + "eur"+str(u)
                    if (c == 3):
                        username = Admin_Dynamic['globalname'] + "gbp"+str(u)
                    if (c == 4):
                        username = Admin_Dynamic['globalname'] + "cad"+str(u)
                    if (c == 5):
                        username = Admin_Dynamic['globalname'] + "aud"+str(u)
                    if (c == 6):
                        username = Admin_Dynamic['globalname'] + "hkd"+str(u)

                    email = username + "@yahoo.com"
                    element.register(c,username,email,password)
                    time.sleep(3)
                    self.navigate_to_page(Admin_Dynamic['CasinoClassicRedDogGameLink'])#user will appeare in dev06
                    time.sleep(3)
                    print("User Created: "+username)
                    element.nothanks()
                    element.logout()
                    element.nothanks()
        if (Admin_Dynamic['createallusers'] == "0"):
            print("Creation of all currency users is not requested")


    def tearDown(self):
            super(createusertest, self).tearDown()

    if __name__ == "__main__":
        # import sys;sys.argv = ['', 'Test.testName']
        # unittest.main()
        nose.main()