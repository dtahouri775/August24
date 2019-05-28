
from BasePage                import BasePage
from AdminAuto.Locators.UIMapRegistration import RegistrationPageMap
from AdminAuto.Locators.UIMapRegistration import UILogInMap
from AdminAuto.Locators.UIMapPromotionCasino import UIpromotion
from BasePage                import IncorrectPageException
import time
class RegisterUserPages(BasePage):

    def __init__(self, driver ):
        super(RegisterUserPages, self).__init__(driver)


    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10,"cssSelector",RegistrationPageMap['LOGIN1'])
            print("Main Login exist!")
        except:
            try:
                self.wait_for_element_visibility(10,"cssSelector", RegistrationPageMap['Join']
                                                 )
            except:
                   raise IncorrectPageException

    def register(self,v,username,email,password):

        #self.fill_out_field("xpath",LogInPageMap['UserNameFieldXpath'], self.username )
        #self.fill_out_field("xpath",LogInPageMap['PasswordFieldXpath'],self.password )
        self.click(10,"cssSelector",RegistrationPageMap['LOGIN1'])
        time.sleep(3)
        self.click(10, "cssSelector", RegistrationPageMap['Join'])
        time.sleep(1)
        self.fill_out_field("cssSelector", RegistrationPageMap['Email'], email)
        time.sleep(1)
        self.click(10, "cssSelector", RegistrationPageMap['Uname'])
        self.fill_out_field("cssSelector", RegistrationPageMap['Uname'], username)
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Upass'])
        self.fill_out_field("xpath", RegistrationPageMap['Upass'], password)
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['UpassConfirm'])
        self.fill_out_field("xpath", RegistrationPageMap['UpassConfirm'],password)
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Reg_Currency_ar'])
        time.sleep(1)

        if (v == 1):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_usd'])
        if (v == 2):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_eur'])
        if (v == 3):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_gbp'])
        if (v == 4):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_cad'])
        if (v == 5):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_aud'])
        if (v == 6):
            self.click(10, "xpath", RegistrationPageMap['Reg_Currency_hkd'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BonusCode'])
        self.fill_out_field("xpath", RegistrationPageMap['BonusCode'], "XANADUINTERNAL")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Phone'])
        self.fill_out_field("xpath", RegistrationPageMap['Phone'], "604786")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Next_b1'])
        time.sleep(3)
        self.click(10, "xpath", RegistrationPageMap['Title_Array'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Title_Gender'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Firstname'])
        self.fill_out_field("xpath", RegistrationPageMap['Firstname'], "fakeUser")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Lastname'])
        self.fill_out_field("xpath", RegistrationPageMap['Lastname'], "fakeUserLastname")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthDay_Array'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthDayDate'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthM_Array'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthMonth'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthYear_Array'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['BirthYear'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Security_Array'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Security_Select'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Security_Answer'])
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Security_Answer'])
        self.fill_out_field("xpath", RegistrationPageMap['Security_Answer'], "XANADU")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['Next_b2'])
        time.sleep(6)
        self.click(10, "xpath", RegistrationPageMap['Country_Array'])
        time.sleep(1)
        #self.fill_out_field("xpath", RegistrationPageMap['Country_Array'], "Ireland")
        time.sleep(1)
        if(v==1):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_usd'])
        if (v == 2):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_eur'])
        if (v == 3):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_gbp'])
        if (v == 4):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_cad'])
        if (v == 5):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_aud'])
        if (v == 6):
            self.click(10, "xpath", RegistrationPageMap['Country_Select_hkd'])

        time.sleep(2)
        self.click(10, "xpath", RegistrationPageMap['AddressL1'])
        self.fill_out_field("xpath", RegistrationPageMap['AddressL1'], "Cork Street 10")
        time.sleep(1)
        self.click(10, "cssSelector", RegistrationPageMap['PostCode'])
        self.fill_out_field("cssSelector", RegistrationPageMap['PostCode'], "4321")
        time.sleep(1)

        self.click(10, "xpath", RegistrationPageMap['AddressL2'])
        self.fill_out_field("xpath", RegistrationPageMap['AddressL2'], "Cork Street 20")
        time.sleep(1)
        self.click(10, "xpath", RegistrationPageMap['CreateAccount'])
        time.sleep(3)
        self.click(10, "xpath", RegistrationPageMap['CloseDepositBox'])
        time.sleep(3)

    def logout(self):

        try:
            self.wait_for_element_visibility(10, "cssSelector", RegistrationPageMap["rhsaccount"])
            element = self.find_element("cssSelector", RegistrationPageMap["rhsaccount"])
            element.click()
            time.sleep(2)
        except:
            print("Info: rhsaccount is not available!")
        self.wait_for_element_visibility(10, "cssSelector", RegistrationPageMap["logout"])
        element2 = self.find_element("cssSelector", RegistrationPageMap["logout"])
        element2.click()
        time.sleep(2)
    def login(self,username,password):
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
            print("CloseDepositBox was not available")

    def verifybonsuicon(self,username):
        try:
            self.wait_for_element_visibility(10, "cssSelector", RegistrationPageMap["BonusIcon"])
            element2 = self.find_element("cssSelector", RegistrationPageMap["BonusIcon"])
            element2.click()
        except:
            raise Exception("This user has not be assigned bonus:  "+username)


    def verifexistingbounstitle(self,bonustitle):
        print("chacking for existance of assigned bonus: "+bonustitle)
        try:
            self.wait_for_element_visibility(10, "cssSelector", UIpromotion["Bonuslink1"])
            element2 = self.find_element("cssSelector", UIpromotion["Bonuslink1"])
            btitle=element2.text
            print("btitle = "+btitle)
            element2.click()
        except:
            raise Exception("This bonus Tiltle is not existing:  " )









