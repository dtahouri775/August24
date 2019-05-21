
from BasePage                import BasePage
from ExchangeSanityAuto.Locators.UIMapMainpage import  LogInPageMap
from BasePage                import IncorrectPageException
import time
class MatchBookLoginPage(BasePage):

    def __init__(self, driver, username,password ):
        super( MatchBookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10,
                                             "cssSelector",
                                             LogInPageMap["LoginButtonTopcssSelector"]
                                             )
        except:
            raise IncorrectPageException

    def login(self):

        self.fill_out_field("xpath",
                            LogInPageMap['UserNameFieldXpath'],
                            self.username
                            )
        self.fill_out_field("xpath",
                            LogInPageMap['PasswordFieldXpath'],
                            self.password
                            )
        self.click(10,
                   "xpath",
                   LogInPageMap['LoginButtonXpath'],
                   )


