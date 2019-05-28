'''
Created on Feb06 , 2019

@author: Daryoush
'''

from AdminAuto.Locators.UIMapAdminPage import AdminHomePageMap
from AdminAuto.Locators.UIMapAdminPage import LogInPageMap
#from AdminAuto.Locators.AdminMapBonusLinks import AdminBonusLinkMap
from AdminAuto.Locators.UIMapLiveTables import AdminTableID
from AdminAuto.Locators.UIMapLiveTables import AdminGameID
from AdminAuto.Locators.UIMapLiveTables import AdminTableName
from AdminAuto.Locators.UIMapLiveTables import AdminSeatTotal
from AdminAuto.Locators.UIMapLiveTables import AdminSeatOpen
from AdminAuto.Locators.UIMapLiveTables import AdminDealerName
from AdminAuto.Locators.UIMapLiveTables import AdminHistory
from AdminAuto.Locators.UIMapBonusPlan import AdminBonusCreationMap
from AdminAuto.Locators.UIMapBonusPlan import AdminBonusInfoMap
#

from BasePage import IncorrectPageException
from BasePage import BasePage
import time

class HomePageM(BasePage):
    def __init__(self, driver):
        super(HomePageM, self).__init__(driver)
        self.fill_out_field("cssSelector",LogInPageMap['UserNameField'],"dtahouri" )
        self.fill_out_field("cssSelector",LogInPageMap['PasswordField'],"Password1")
        self.click(10,"cssSelector",LogInPageMap['LoginButton'])


        #
        '''
        global TableID
        global GameID
        global TableName
        global PlayerNum
        global SeatTotal
        global SeatOpent
        global Dealername
        global History
        '''

    def _verify_page(self):
        self.wait_for_element_visibility(10, "cssSelector", LogInPageMap['LoginButton'])
        self.wait_for_element_visibility(10, "cssSelector", LogInPageMap['UserNameField'])
        self.wait_for_element_visibility(10, "cssSelector", LogInPageMap['PasswordField'])



    def clickAdminstration(self):

        try:
            self.driver.get("http://dev06.xcl.ie:20194/j/LiveTablesEvo.action")
            gamename = self.wait_for_element_visibility(10, "xpath", AdminHistory["HistoryTab"])
            gamename = self.find_element("xpath", AdminHistory["HistoryTab"])
            gamename.click()
            time.sleep(1)
            gamename.click()
            time.sleep(1)

        except:
            raise IncorrectPageException

    def matrixtest(self):
        lsthistory = []
        m = 84  # Number of raw
        n = 7  # Number of column
        for i in range(0, m):
            lsthistory.append([])


        for i in range(0, m):
            for j in range(0, n):
                lsthistory[i].append(j)
                lsthistory[i][j] = "Raw"+str(i)
            lsthistory[i][j] = "Gol" + str(j)

        print("inside matrix", lsthistory)
    def recordDreamCatcherResultsfromadmin(self,i):

        try:


            lsthistory = []

            #AdminLiveTableID
            tempng1 = "AdminLiveTableID" + str(i)
            gamename = self.wait_for_element_visibility(10, "xpath", AdminTableID[tempng1])
            gamename = self.find_element("xpath", AdminTableID[tempng1])
            lsthistory.append(gamename.text)
            #AdminLiveGameID
            tempng2 = "AdminLiveGameID" + str(i)
            gameid = self.wait_for_element_visibility(10, "xpath", AdminGameID[tempng2])
            gameid = self.find_element("xpath", AdminGameID[tempng2])
            lsthistory.append(gameid.text)
            #AdminLiveTableName
            tempng3 = "AdminLiveTableName" + str(i)
            tablename = self.wait_for_element_visibility(10, "xpath", AdminTableName[tempng3])
            tablename = self.find_element("xpath", AdminTableName[tempng3])
            lsthistory.append(tablename.text)
            #AdminLiveSeatTotal1
            tempng4 = "AdminLiveSeatTotal" + str(i)
            seattotal = self.wait_for_element_visibility(10, "xpath", AdminSeatTotal[tempng4])
            seattotal = self.find_element("xpath", AdminSeatTotal[tempng4])
            lsthistory.append(seattotal.text)
            #AdminLiveSeatOpen
            tempng5 = "AdminLiveSeatOpen" + str(i)
            seatopen = self.wait_for_element_visibility(10, "xpath", AdminSeatOpen[tempng5])
            seatopen = self.find_element("xpath", AdminSeatOpen[tempng5])
            lsthistory.append(seatopen.text)
            #AdminLiveDealerName
            tempng6 = "AdminLiveDealerName" + str(i)
            dealername = self.wait_for_element_visibility(10, "xpath", AdminDealerName[tempng6])
            dealername = self.find_element("xpath", AdminDealerName[tempng6])
            lsthistory.append(dealername.text)
            tempng7 = "AdminLiveHistory" + str(i)
            gamehistory = self.wait_for_element_visibility(10, "xpath", AdminHistory[tempng7])
            gamehistory = self.find_element("xpath", AdminHistory[tempng7])
            lsthistory.append(gamehistory.text)
                #print("Info text=", lsthistory[i])
            return lsthistory


        except:
            raise IncorrectPageException

    def assignbonus(self,pname,i):
        try:
            if(i!=1000):
                try:
                    tempng1="AssignArrow"
                    self.wait_for_element_visibility(10, "xpath",AdminHomePageMap[tempng1])
                    self.find_element("xpath", AdminHomePageMap[tempng1]).click()
                except:
                    self.click(10, "xpath", AdminBonusCreationMap["assignplayerbutton"])
                    time.sleep(3)

            self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['UserListEditbox'])
            self.find_element("xpath", AdminHomePageMap['UserListEditbox'])
            self.click(10, "xpath",  AdminHomePageMap['UserListEditbox'])
            self.fill_out_field("xpath",  AdminHomePageMap['UserListEditbox'], pname)
            time.sleep(3)
            if(i==6):
                try:
                    self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['DepositAmountBox'])
                    element = self.find_element("xpath", AdminHomePageMap['DepositAmountBox'])
                    self.click(10, "xpath", AdminHomePageMap['DepositAmountBox'])
                    self.fill_out_field("xpath", AdminHomePageMap['DepositAmountBox'], "10")
                    time.sleep(1)
                    self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['AssignButtonDeposit'])
                    element = self.find_element("xpath", AdminHomePageMap['AssignButtonDeposit'])
                    element.click()
                    time.sleep(3)
                except:
                    print("Info: Can not fill Deposite Box!!")

            time.sleep(1)
            try:
                self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['AssignButton'])
                element=self.find_element("xpath", AdminHomePageMap['AssignButton'])
                element.click()
                time.sleep(3)
            except:
                print("AssignButton Deposite Box has been clicked already!!")
            try:
                self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['Assignconfirmationfail'])
                element = self.find_element("xpath", AdminHomePageMap['Assignconfirmationfail'])
            except:
                print("Info: has not been failed, it is in Pass process!!")
                self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['Assignconfirmationpass'])
                element = self.find_element("xpath", AdminHomePageMap['Assignconfirmationpass'])

            return element.text
            #Assignconfirmationitext
            #AssignButton
            #UserListEditbox

        except:
            raise IncorrectPageException

    def gotoselectedbonus(self,url):
        try:
            time.sleep(3)
            self.driver.get(AdminBonusCreationMap[url])
            time.sleep(3)
        except:
            raise IncorrectPageException


    def   createbonusplan(self,pname, pr, cur, tt, st, sdate, edate,exd, amount, rr, mbl, ucr, fdg, fmg, ips, igs):
        try:
            self.wait_for_element_visibility(10, "xpath", AdminBonusCreationMap['pnamebox'])
            element = self.find_element("xpath", AdminBonusCreationMap['pnamebox'])
            self.click(10, "xpath", AdminBonusCreationMap['pnamebox'])
            self.fill_out_field("xpath", AdminBonusCreationMap['pnamebox'], pname)
            time.sleep(1)
            print("Plan Name is entered!")
            #priority
            self.wait_for_element_visibility(10, "xpath", AdminBonusCreationMap['periority'])
            element = self.find_element("xpath", AdminBonusCreationMap['periority'])
            self.click(10, "xpath", AdminBonusCreationMap['periority'])
            self.fill_out_field("xpath", AdminBonusCreationMap['periority'], pr)
            time.sleep(1)
            print("Priority is entered!")
            #Trigger Type
            trigertype = "trigertype" +str(tt)
            self.wait_for_element_visibility(10, "xpath", AdminBonusCreationMap[trigertype])
            element = self.find_element("xpath", AdminBonusCreationMap[trigertype])
            self.click(10, "xpath", AdminBonusCreationMap[trigertype])
            time.sleep(1)
            print("Trigger Type is Selected!")
            #Status
            status = "status" + str(st)
            self.wait_for_element_visibility(10, "xpath", AdminBonusCreationMap[status])
            element = self.find_element("xpath", AdminBonusCreationMap[status])
            self.click(10, "xpath", AdminBonusCreationMap[status])
            time.sleep(1)
            print("Status Type is Selected!")
            #Start Date
            #self.driver.findElement(By.id("dp1557952495805")).click()

            self.wait_for_element_visibility(10, "name",AdminBonusCreationMap['startdate'])
            element = self.find_element("name", AdminBonusCreationMap['startdate'])
            self.click(10, "name", AdminBonusCreationMap['startdate'])
            self.fill_out_field("name", AdminBonusCreationMap['startdate'], sdate)
            time.sleep(1)
            print("Start date is entered!")
            self.click(10, "xpath", AdminBonusCreationMap['pnamebox'])#click somewhere else to make sure end date is visible
            #End Date
            self.wait_for_element_visibility(10, "name", AdminBonusCreationMap['enddated'])
            element = self.find_element("name", AdminBonusCreationMap['enddated'])
            self.click(10, "name", AdminBonusCreationMap['enddated'])
            self.fill_out_field("name", AdminBonusCreationMap['enddated'],edate)
            time.sleep(1)
            print("End date is entered!")
            self.click(10, "xpath", AdminBonusCreationMap['pnamebox'])  # click somewhere else
            curencytype="currency"+str(cur)
            #Currencies type
            self.click(10, "xpath", AdminBonusCreationMap["currency"])
            self.click(10, "xpath", AdminBonusCreationMap[curencytype])

#Bonus Properties

            element = self.find_element("xpath", AdminBonusCreationMap["expirydate"])
            self.click(10, "xpath", AdminBonusCreationMap["expirydate"])
            self.fill_out_field("xpath", AdminBonusCreationMap['expirydate'], exd)
            time.sleep(1)
            print("Expiry date is filled!")
            element = self.find_element("xpath", AdminBonusCreationMap["amount"])
            self.click(10, "xpath", AdminBonusCreationMap["amount"])
            self.fill_out_field("xpath", AdminBonusCreationMap['amount'], amount)
            time.sleep(1)
            print("amount is filled!")
            element = self.find_element("xpath", AdminBonusCreationMap["roloverrequirement"])
            self.click(10, "xpath", AdminBonusCreationMap["roloverrequirement"])
            self.fill_out_field("xpath", AdminBonusCreationMap['roloverrequirement'], rr)
            time.sleep(1)
            print("roloverrequirement is filled!")
            element = self.find_element("xpath", AdminBonusCreationMap["maxbetlimit"])
            self.click(10, "xpath", AdminBonusCreationMap["maxbetlimit"])
            self.fill_out_field("xpath", AdminBonusCreationMap['maxbetlimit'], mbl)
            time.sleep(1)
            print("Maxbetlimit is filled!")
            if(tt==3):#MB free spins values
                self.click(10, "name", AdminBonusInfoMap["coinvalue"])
                cv = "4"
                self.fill_out_field("name", AdminBonusInfoMap['coinvalue'], cv)
                time.sleep(1)
                element=self.find_element("xpath", "/html/body/div[1]/div/form/table/tbody/tr[22]/td[2]/table/tbody/tr[2]/td[2]/input")
                element.click()
                bpl = "5"
                #element.click()
                self.fill_out_field("xpath", "/html/body/div[1]/div/form/table/tbody/tr[22]/td[2]/table/tbody/tr[2]/td[2]/input",bpl)
                time.sleep(1)
                self.click(10, "name", AdminBonusInfoMap["numberoflines"])
                nl = "5"
                self.fill_out_field("name", AdminBonusInfoMap['numberoflines'], nl)
                time.sleep(1)

            if(tt==4):
                element = self.find_element("xpath","/html/body/div[1]/div/form/table/tbody/tr[20]/td[2]/input")
                element.click()
                bpl = "5"
                # element.click()
                self.fill_out_field("xpath","/html/body/div[1]/div/form/table/tbody/tr[20]/td[2]/input",bpl)
            if(tt==5):
                self.click(10, "xpath", AdminBonusInfoMap["rtstake"])
                time.sleep(1)
                self.click(10, "xpath", AdminBonusInfoMap["rtstake8"])

            if(ucr==0):
                self.click(10, "xpath", AdminBonusCreationMap["usecontributionrate"])
            if (fdg == 0):
                self.click(10, "xpath", AdminBonusCreationMap["fordesktopgames"])
            if (fmg == 0):
                self.click(10, "xpath", AdminBonusCreationMap["formobilegames"])
            if (ips == 0):
                self.click(10, "xpath", AdminBonusCreationMap["includedplatformcheckall"])
            if (igs == 1):
                self.click(10, "xpath", AdminBonusCreationMap["includegamescheckall"])

        #Other Properties
            self.click(10, "xpath", AdminBonusCreationMap["notes"])
            text="Notes:  "+pname
            self.fill_out_field("xpath", AdminBonusCreationMap['notes'],text)

            self.click(10, "xpath", AdminBonusCreationMap["bonustitle"])
            text = "Bonus Title:  " + pname
            self.fill_out_field("xpath", AdminBonusCreationMap['bonustitle'], text)

            self.click(10, "name", AdminBonusCreationMap["bonusdescription"])
            text = "Bonus Description:  " + "Plan name= "+pname
            self.fill_out_field("name", AdminBonusCreationMap['bonusdescription'], text)

            self.click(10, "xpath", AdminBonusCreationMap["bonusdetail"])
            text = "Bonus Details:  " + "Plan name= " + pname
            self.fill_out_field("xpath", AdminBonusCreationMap['bonusdetail'], text)

            self.click(10, "xpath", AdminBonusCreationMap["termandcondition"])
            text = "Bonus Terms and Conditions:  " + "Plan name= " + pname
            #self.click(10, "xpath", AdminBonusCreationMap["termandcondition"])
            self.fill_out_field("xpath", AdminBonusCreationMap['termandcondition'], text)

            time.sleep(1)
            if(tt==7):#held fund bonu
                self.click(10, "name", AdminBonusCreationMap["claimamounthf"])
                text = "1,5,10"
                self.fill_out_field("name", AdminBonusCreationMap['claimamounthf'], text)
                #openToAll
                self.click(10, "name", AdminBonusCreationMap["openToAll"])

            self.click(10, "xpath", AdminBonusCreationMap["savebutton"])
            time.sleep(2)
            element = self.find_element("xpath", AdminBonusCreationMap["success"])
            temp=element.text
            print(temp)
            if (temp == "Success"):
                print("Bonus created")
            if (temp != "Success"):
                print("Fail: Bonus is not created!")
            return temp
            '''
            if(plassign==1):
                self.click(10, "xpath", AdminBonusCreationMap["assignplayerbutton"])
                time.sleep(3)
                self.wait_for_element_visibility(10, "xpath", AdminHomePageMap['UserListEditbox'])
                self.find_element("xpath", AdminHomePageMap['UserListEditbox'])
                self.click(10, "xpath", AdminHomePageMap['UserListEditbox'])
                self.fill_out_field("xpath", AdminHomePageMap['UserListEditbox'], playernames)
                time.sleep(2)
             '''



        except:
            raise IncorrectPageException
        
