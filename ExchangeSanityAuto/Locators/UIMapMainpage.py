'''
Created on Sept 17, 2018

@author: Daryoush
'''

#note the relative xpath may not function on some of the explore or version of explores.

MainPageMapXpath = dict(
                          searchcasinoLocator = "[data-hook='search-top']",
                          Usernametitle ="[data-hook='login-username']",
                          #Usernametitle =".Account__title___1q0Mb",#will edit when correct data hook is implemented
                          topcasinoLocatorXpath = "[data-hook='casino-top']",
                          logout ="[data-hook='logout']",
                          rhsaccount ="[data-hook='rhsaccount']",#added Jan 2019

                          BetSlipBack = "[data-hook='betslip-back']",
                          BetSlipStake = "[data-hook='betslip-stake']",
                          BetSlipProfit = "[data-hook='betslip-profit']",
                          BetSlipProfitmatched = ".Bet__layersStake___2Fn0q > span:nth-child(1)",##do not have tag
                          BetSlipcheckmark =".mb-button--confirm > svg:nth-child(1)",#do not have tag
                          BetSlipadd="[data-hook='betslip-add']",#assigned data hook is not functioning! may be because of + sing?
                          #BetSlipadd=".mb-offer-row__control-increase-odds",
                          BetSlipdeduct="[data-hook='betslip-deduct']",

                          ReviewOrderPlaceBet = "a.ReviewOffer__button___laKsM:nth-child(2)",#do not have tag
                          ReviewOrderCancelBet = "a.ReviewOffer__button___laKsM:nth-child(1)",#do not have tag


                          UpdatedOffervalueback ="[data-hook='popular-markets--market-0--runner-0--price-0-back']",
                          UpdatedOffervaluelay ="[data-hook='popular-markets--market-0--runner-0--price-0-lay']",
                          UpdatedOffervaluewin="[data-hook='popular-markets--market-0--runner-0--price-0-win']",
                          sec2BackMakeOffer = "[data-hook='popular-markets--market-0--runner-0--price-0-back']",

                          sec2LayMakeOffer = "[data-hook='popular-markets--market-0--runner-0--price-0-lay']",
                          BetSlipLay = "[data-hook='betslip-back']",

                          BetSlipLayStake = "[data-hook='betslip-stake']",

                          BetSlipLaycheckmark =".mb-button--confirm > svg:nth-child(1)",#do not have tag
                          BetSlipunmatchedmenu ="[data-hook='betslip-unmatched-menu']",

                          DeleteButtonUnmatched = "[data-hook='unmatched-redx']",
                          serRightTopnametest="[data-hook='loginusername']",

                         DisplaySettingPopup="[data-hook='display-settings']",
                         DisplayDetailExchangeTypecheckbox= "[data-hook='display-settings-exchange-type']",
                         DisplayDetailExchangeUpdate ="[data-hook='settings-update']",
                         DisplayDetailExchangeDiscard="[data-hook='settings-discard']",
                        AcceptCookiesButton ="[data-hook='acceptcookies']",
                        NothanksXpath ="[data-hook='nothanks']",
                        #matched at the top
                        Matchedmenu="[data-hook='betslip-matched-menu']",
                        MatchedTotAmount = ".Bet__layersStake___2Fn0q > span:nth-child(1)",#amount of matched in third edit box,#do not have tag

                        SelectMatchwon = "[data-hook='popular-markets--market-0--runner-0--price-0-win']", #Horse racing firs spot win offer Windsor
                        SelectMatchLose="[data-hook='popular-markets--market-0--runner-0--price-0-lose']",# Horse racing firs spot lose offer

                        #Odds in Display Detail
                        DisplayOddsArrow="[data-hook='display-odds-type']",#Display
                        DisplayOddsUsd="[data-hook='display-usodds']",
                        DisplayOddsDecimal="[data-hook='display-decimalodds']",
                        DisplayOddsHkd="[data-hook='display-hkodds']",#Display
                        DisplayOddsMalay="[data-hook='display-malayodds']",#Display

                        #when bet is more than available fund player will be prompted for deposit
                        DepositDilagbox=".mb-modal__header__icon > g:nth-child(2) > g:nth-child(1) > polygon:nth-child(1)",#do not have tag
                        Availablebalance="div.Balances__item___18HEP:nth-child(3) > div:nth-child(2)",#available balance for player   #do not have tag

                        #multiple offer test selected from Arsenal VS Tottenham and Windsor
                        HorseRaceWin3= "[data-hook='popular-markets--market-0--runner-2--price-0-win']",
                        HorseRaceWin4="[data-hook='popular-markets--market-0--runner-3--price-0-win']",
                        HorseRaceLose5="[data-hook='popular-markets--market-0--runner-4--price-0-lose']",
                        AvsTDrawWin3="[data-hook='popular-markets--market-1--runner-2--price-0-win']",
    #edit box expath:


                        BS1W = "[data-hook='betslip-back']",#data hook is the same for different boxes and needs to be fixed, in every page the dat-hook name should be unique for each element
                        BS1S = "[data-hook='betslip-stake']",
                        BS2W = ".Offer__odds--lose___17J8k > span:nth-child(1) > input:nth-child(2)",#proper data-hook is required
                        BS2S = ".Offer__backersStake--lose___3xTQp > span:nth-child(1) > input:nth-child(2)",
                        BS3W = "div.Offer__containerOfferRows___2Mz23:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > input:nth-child(2)",
                        BS3S = "div.Offer__containerOfferRows___2Mz23:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > input:nth-child(2)",
                        BS4W = "div.Offer__containerOfferRows___2Mz23:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > input:nth-child(2)",
                        BS4S = "div.Offer__containerOfferRows___2Mz23:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > input:nth-child(2)",

                        BS1Check="div.Offer__containerOfferRows___2Mz23:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > svg:nth-child(1)",#do not have tag
                        BS2Check="div.Offer__containerOfferRows___2Mz23:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)",#do not have tag
                        BS3Check="div.Offer__containerOfferRows___2Mz23:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)",#do not have tag
                        BS4Check="div.Offer__containerOfferRows___2Mz23:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)",#do not have tag

                        Nothanksbutton="[data-hook='no-thanks']",


                     )


LogInPageMap = dict(  LoginButtonTopcssSelector="[data-hook='login-top']",#custom hook
                      LogInToMatchbookTextXpath  = "/html/body/div[3]/div/div/div/div[1]/span",#do not have tag
                      UserNameFieldXpath  = "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[1]/div[1]/div/input",#do not have tag

                      PasswordFieldXpath   = "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[1]/div[2]/div/input",#do not have tag
                      LoginButtonXpath      = "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[2]/a[1]",#do not have tag
                      ForgotPasswordXpath    = "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/span/div/form/div[2]/a[2]",#do not have tag
                      JoinMatchbook    = "[data-hook='registration-top']",#custom hook
                      BetNowButtonXpath = "//*[@id='mb-join-now-right-image']"#has not used
)

#No thanks when logout xpath
#/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/a[2]