'''
Created on Feb06 , 2019

@author: Daryoush
'''
AdminHomePageMap = dict(
                        Dashboard="#menuList > li:nth-child(1) > span:nth-child(2)",
                        Administration="#menuList > li:nth-child(2) > span:nth-child(2)",
                        Reports = "li.closed:nth-child(3) > span:nth-child(2)",
                        Promotion = "/html/body/div[1]/div[2]/ul/li[5]/span",
                           RegularPromotion="/html/body/div[1]/div[2]/ul/li[5]/ul/li/span",
                             ListBonusPlans= "/html/body/div[1]/div[2]/ul/li[5]/ul/li/ul/li[2]/span/a",
                                PlanNameBox = "/html/body/div[1]/form/div/table/thead/tr[2]/td[3]/div",
                                               SearchIcon="/html/body/div[1]/form/div/table/thead/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td[13]/a/img",
                                        AssignArrow="/html/body/div[1]/form/div/table/tbody/tr/td[1]/a[5]",
                                            UserListEditbox="/html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/textarea",
                                                AssignButton="/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/input",
                                                AssignButtonDeposit="/html/body/div[1]/div/form/table/tbody/tr[5]/td[2]/input",
                                                    Assignconfirmationfail="/html/body/div[1]/div/div[2]/ul/li[2]",
                                                    Assignconfirmationpass="/html/body/div[1]/div/div[2]/ul/li",
                        GameAdmin = ".collapsable > ul:nth-child(3) > li:nth-child(1) > span:nth-child(2)",
                        GameControl = "li.collapsable:nth-child(1) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(1) > a:nth-child(1)",
                        AddnewGame = "li.collapsable:nth-child(1) > ul:nth-child(3) > li:nth-child(2) > span:nth-child(1) > a:nth-child(1)",
                        EvolutionTables = "li.collapsable:nth-child(1) > ul:nth-child(3) > li:nth-child(3) > span:nth-child(1) > a:nth-child(1)",
                        LiveTableEvo = "li.collapsable:nth-child(1) > ul:nth-child(3) > li:nth-child(4) > span:nth-child(1) > a:nth-child(1)",
                        LiveTableNetEnt="li.collapsable:nth-child(1) > ul:nth-child(3) > li:nth-child(5) > span:nth-child(1) > a:nth-child(1)",
                        JackpotInfoList="li.last:nth-child(6) > span:nth-child(1) > a:nth-child(1)",
                        MainDashboard ="#menuList > li:nth-child(1) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(2)",
                        PlayerDashboard ="li.expandable:nth-child(2) > span:nth-child(2)",
                        DepositAmountBox="//*[@id='depositAmount']"
                        )
LogInPageMap = dict(
                      UserNameField="#userName",
                      PasswordField="#password",
                      LoginButton="#submit",
)

