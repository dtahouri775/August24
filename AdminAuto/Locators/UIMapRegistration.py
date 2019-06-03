'''
Created on April30 , 2019

@author: Daryoush
'''
RegistrationPageMap = dict(
    Nothanksbutton="[data-hook='no-thanks']",
    LOGIN1="[data-hook='login-top']",
    Join= "[data-hook='loginjoinnow']",

    # Css for Email field
    Email="[data-hook='register-email']",
    # Css for User name field
    Uname="[data-hook='register-username']",
    # Css for Password field
    Upass="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/input",
    # Css for Confirm Password field
    UpassConfirm="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[4]/div/input",
    # Currency arrow drpon down

    Reg_Currency_ar="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[1]/a/i",
    # XPATH for usd currency
    Reg_Currency_usd="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[1]/div",
    # XPATH for EUR currency
    Reg_Currency_eur="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[2]/div",
    # XPATH for EUR currency
    Reg_Currency_gbp="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[3]/div",
    # XPATH for CAD currency
    Reg_Currency_cad="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[4]/div",
    # XPATH for AUD currency
    Reg_Currency_aud="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[5]/div",
    # XPATH for HKD currency
    Reg_Currency_hkd="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[1]/div/div/div[2]/span/div/div[1]/div/div[6]/div",

    BonusCode="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div[2]/div/input",
    BonusIcon=".bonus-toggle-icon",
    # Xpath for Phone number edit box 5 digit at least
    Phone="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[6]/div/input",
    # css for next button
    Next_b1="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[2]/a",

    # Css for title array
    Title_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[1]/div[1]/div/div/div[1]/a/i",

    # css for Title "Mr"
    Title_Gender="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[1]/div[1]/div/div/div[2]/span/div/div/div/div[1]/div",

    # css for First name
    Firstname="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[1]/div[2]/div/input",
    # css for Last name
    Lastname="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[2]/div/input",
    # css for day of birthday arrow
    BirthDay_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[1]/div/div[1]/a/i",
    # css for day of birthday "1"
    BirthDayDate="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[1]/div/div[2]/span/div/div[1]/div/div[2]/div",
    # css for Month of birthday array
    BirthM_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[2]/div/div[1]/a/i",

    # css for Month of birthday "January"
    BirthMonth="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[2]/div/div[2]/span/div/div[1]/div/div[1]/div",
    # css for Year of birthday array
    BirthYear_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[3]/div/div[1]/a/i",
    # css for Year of birthday "1999"
    BirthYear="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/div[3]/div/div[2]/span/div/div[1]/div/div[3]/div",
    # Securiry question array
    Security_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[4]/div/div/div[1]/a/i",
    # Securiry question "Your First School
    Security_Select="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[4]/div/div/div[2]/span/div/div/div/div[3]/div",
    # Css Security Answer
    Security_Answer="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[5]/div/input",
    # Css Next Step after about you
    Next_b2="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[2]/a",

    #########Address########
    # Xpath country array
    Country_Array="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[1]/div/div/div/input",

    # //*[@id='option-0']#Afghanistan
    # //*[@id='option-1']#Albania
    Country_Select_eur="//*[@id='option-81']",#irland
    Country_Select_gbp="//*[@id='option-184']",#United Kingdom
    Country_Select_usd="//*[@id='option-82']",#Isle of Man
    Country_Select_cad="//*[@id='option-82']",#Isle of Man
    Country_Select_aud="//*[@id='option-9']",  # Austeralia

    Country_Select_hkd="//*[@id='option-74']",#HonkKong
    Country_Select_gibeur="//*[@id='option-63']",#Gibralta
    Country_Select_gibgbp="//*[@id='option-63']",#Gibralta
    #//*[@id="option-63"]#Gibralta



    # css Post code
    #PostCode="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[2]/div/input",
PostCode="[data-hook='register-postcode']",
#data-hook="register-postcode"
    # css Address Line 1
    AddressL1="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[3]/div/input",
    # css Address Line 2
    AddressL2="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[1]/form/div/div/div[4]/div/input",
    # create an account button
    CreateAccount="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/div[2]/a",
    # Css Close Dialogbox
    CloseAndJoin=".mb-modal__header__icon > g:nth-child(2) > g:nth-child(1) > polygon:nth-child(1)",
    #Feebacktest="body > div.ReactModalPortal > div > div > div > div.mb-modal__content > div > div.Feedback__containerInput___3s20S > textarea",
    Table_Real_Play="[data-hook='casino-landing-page-betlimit1']",
    CloseDepositBox="/html/body/div[3]/div/div/div/div[1]/div",

#data-hook="register-postcode"
    rhsaccount="[data-hook='rhsaccount']",
    logout="[data-hook='logout']",
    #

)
LogInPageMap = dict(
                      UserNameField="#userName",
                      PasswordField="#password",
                      LoginButton="#submit",
)

UILogInMap = dict(  PlayforFun="[data-hook='casino-landing-page-play-for-fun']",

                      LoginButtonTop="[data-hook='login-top']",

                      LoginLandingPage1="[data-hook='casino-landing-page-betlimit1']",
                      LoginLandingPage2="[data-hook='casino-landing-page-betlimit2']",
                      LoginLandingPage3="[data-hook='casino-landing-page-betlimit3']",
                      LoginLandingPage4="[data-hook='casino-landing-page-betlimit4']",
                      LivePlaynow ="[data-hook='live-casino-play-now']",
                      LogInToMatchbookTextXpath="/html/body/div[3]/div/div/div/div[1]/span",#will modify when data hook is available
                      UserNameFieldXpath="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[1]/div[1]/div/input",#will modify when data hook av
                      PasswordFieldXpath="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[1]/div[2]/div/input",#will modify when data hook av
                      LoginButtonXpath="/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[2]/a[1]",#will modify when data hook av
                      ForgotPasswordXpath= "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[2]/a[2]",#will modify when data hook av
                      JoinNowXpath="//*[@id='mb-join-now-button']",#will modify when data hook is available
                      BetNowButtonXpath="//*[@id='mb-join-now-right-image']"#will modify when data hook is available
                  )
