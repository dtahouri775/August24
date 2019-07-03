import win32api, win32con#For Mouse activity
from AdminAuto.Locators.UIMapRegistration import RegistrationPageMap
from AdminAuto.Locators.UIMapRegistration import UILogInMap
#from AdminAuto.Locators.UIMapPromotionCasino import UIpromotion
from BasePage                import BasePage
import time
class GamePlayPage(BasePage):

    def __init__(self, driver, username, password):
        super(GamePlayPage, self).__init__(driver)
        self.username = username
        self.password = password

    def login(self):
        username = self.username
        password = self.password
        self.wait_for_element_visibility(10, "cssSelector", RegistrationPageMap["LOGIN1"])
        element2 = self.find_element("cssSelector", RegistrationPageMap["LOGIN1"])
        element2.click()

        self.fill_out_field("xpath",
                            UILogInMap['UserNameFieldXpath'],
                            username
                            )
        self.fill_out_field("xpath",
                            UILogInMap['PasswordFieldXpath'],
                            password
                            )
        self.click(10,
                   "xpath",
                   UILogInMap['LoginButtonXpath'],
                   )

        try:
            time.sleep(3)
            self.click(10, "xpath", RegistrationPageMap['CloseDepositBox'])
            time.sleep(3)
        except:
            print("CloseDepositBox was not available on log in")
    def clickme(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    def installflashgame(self):
        try:
            self.clickme(905, 555)
            print("Click Here Pressed")
            time.sleep(1)
        except:
            print("Did not click flash install")
            print("install Flash")
        try:
            self.clickme(300, 150)
            print("Allow is Pressed")
            time.sleep(1)
        except:
            print("Did not click flash install")
            print("install Flash")

    def acceptcookies(self):
        try:
            element = self.find_element("cssSelector", UILogInMap["AcceptCookies"])
            element.click()
        except:
            print("Bug Cookies dialog box is not there")

    def nothanks(self):
        #self.navigate_to_page("https://dev06.xcl.ie/casino/play/PL49/T0002?limit=0")
        try:
            element3 = self.find_element("cssSelector", RegistrationPageMap["Nothanksbutton"])
            print("Info No thanks button is found")
            element3.click()
            print("Info No thanks button is clicked")
        except:
            print "Info No thanks button is not there to cause bug"

    def gotoblackjacklimit0(self):
        try:
            time.sleep(3)
            self.driver.get("https://dev06.xcl.ie/casino/play/PL49/T0002?limit=0")
            time.sleep(3)
        except:
            print("Bug: Can not Navigate to requested lin")
    def playbjgames(self,a):

        self.placeseatbetbj(1)#1 means first seat in black jack game (the most left on the game screen)
        time.sleep(1)
        self.placeseatbetbj(2)
        time.sleep(1)
        self.placeseatbetbj(3)
        time.sleep(1)
        self.pressDealbuttonbj()
        time.sleep(15)
        self.presStandButtonbj(3)
        time.sleep(15)
        v2=""
        v3=""
        v4=""
        for i in range(1, a):
            print("gnum= "+str(i))
            self.rebetdealblackjack(3)#in case ther is insurance other wise 1 was good enough
            time.sleep(5)
            self.presStandButtonbj(3)
            if(i%2==0):
                v2=""+self.returnavailablebalance()
                #print("v2="+str(v2))
            if(i%3==0):
                v3 = ""+self.returnavailablebalance()
                #print("v3=" + str(v3))
            if(i%4==0):
                v4 = ""+self.returnavailablebalance()
                #print("v4=" + str(v4))
            if(v2==v3 and v2==v4 and v2!=""):
                self.gotoblackjacklimit0()
                time.sleep(30)
                self.placeseatbetbj(1)  # 1 means first seat in black jack game (the most left on the game screen)
                time.sleep(1)
                self.placeseatbetbj(2)
                time.sleep(1)
                self.placeseatbetbj(3)
                time.sleep(1)
                self.pressDealbuttonbj()
                time.sleep(15)
                self.closeunfinishedmessage()#incase the game is in unfinished status
                self.presStandButtonbj(3)
                self.gotoblackjacklimit0()
                time.sleep(30)
                self.placeseatbetbj(1)  # 1 means first seat in black jack game (the most left on the game screen)
                time.sleep(1)
                self.placeseatbetbj(2)
                time.sleep(1)
                self.placeseatbetbj(3)
                time.sleep(1)
                self.pressDealbuttonbj()
                time.sleep(15)
                self.presStandButtonbj(3)
                time.sleep(15)

    def closeunfinishedmessage(self):
        try:
            self.clickme(1225, 705)
            self.clickme(1220, 705)
            self.clickme(1225, 710)
            print("Unfinished Close massage is clicked")
        except:
            print("Bug: Unfinished Close massage is not clickedd")


    def returnavailablebalance(self):
        try:

            self.wait_for_element_visibility(10, "cssSelector", UILogInMap['Availablebalance'])

            element3 = self.find_element("cssSelector",UILogInMap['Availablebalance'])
        except:  #
            print("Available balance is not available Bug :101")

        text1 = element3.get_attribute('innerText')
        return text1




    def placeseatbetbj(self,s):
        time.sleep(2)

        if(s==1):
            try:
                self.clickme(1380, 760)
                print("minimum bet is located in the first seat")
            except:
                print("BJ first seat bet is not handled")
        if (s == 2):
            try:
                self.clickme(990, 865)
                print("minimum bet is located in the Second seat")
            except:
                print("BJ Second seat bet is not handled")
        if (s == 3):
            try:
                self.clickme(600,760)
                print("minimum bet is located in the thired seat")
            except:
                print("BJ Second seat bet is not handled")
    def pressDealbuttonbj(self):

        try:
            self.clickme(1210, 700)
            time.sleep(1)
            print("Deal Button is Pressed")
        except:
            print("Bug: Deal Button is not Pressed")
            time.sleep(5)
    def presStandButtonbj(self,n):

        try:
            for i in range(1,n+1):
                self.clickme(1365, 1110)
                print("Stand Button is clicked"+str(n))
                time.sleep(2)

        except:
            print("Bug: Stand Button is Not clicked!!")

    def rebetdealblackjack(self,n):#it covers for No to insurance all

        try:
            for i in range(1,n+3):
                self.clickme(1525, 1110)
                time.sleep(1)
                print("Rebet and Deal is clicked"+str(n))
                #when dealer has blackjack
                '''
                if(i==5):
                    self.placeseatbetbj(1)  # 1 means first seat in black jack game (the most left on the game screen)
                    time.sleep(1)
                    self.placeseatbetbj(2)
                    time.sleep(1)
                    self.placeseatbetbj(3)
                    #time.sleep(1)
                '''

                #time.sleep(2)

        except:
            print("Bug: Rebet and Deal  is Not clicked!!")