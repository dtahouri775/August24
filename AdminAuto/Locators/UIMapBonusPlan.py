AdminBonusCreationMap = dict(
    linkcreatebonus="http://dev06.xcl.ie:20194/j/bonus/CreateBonusPlan.action",
    linkEur1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1185",
    linkAud1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1420",
    linkUsd1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1422",
    linkHkd1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1421",
    linkGbp1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1424",
    linkCad1M="http://dev06.xcl.ie:20194/j/bonus/AssignBonusBatch.action?bonusPlanId=1423",
    pnamebox="/html/body/div[1]/div/form/table/tbody/tr[2]/td[2]/input",
    periority="/html/body/div[1]/div/form/table/tbody/tr[3]/td[2]/input",
    trigertype1 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[1]",#Regular
    trigertype2 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[2]",#
    trigertype3 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[3]",#
    trigertype4 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[4]",#
    trigertype5 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[5]",#
    trigertype6 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[6]",#
    trigertype7 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[7]",#
    trigertype8 = "/html/body/div[1]/div/form/table/tbody/tr[4]/td[2]/select/option[8]",#


    status1 = "/html/body/div[1]/div/form/table/tbody/tr[5]/td[2]/select/option[1]",#Active
    status2 = "/html/body/div[1]/div/form/table/tbody/tr[5]/td[2]/select/option[2]",#Not Active

    startdate = "startDate",
                #//*[@id="dp1557952495805"]

    enddated = "endDate",
    currency = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select",
    currency1 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[1]",
    currency2 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[2]",
    currency3 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[3]",
    currency4 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[4]",
    currency5 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[5]",
    currency6 = "/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[6]",
    #/html/body/div[1]/div/form/table/tbody/tr[8]/td[2]/select/option[1]
    expirydate = "/html/body/div[1]/div/form/table/tbody/tr[12]/td[2]/input",
    amount="/html/body/div[1]/div/form/table/tbody/tr[13]/td[2]/input",
    maxamount="/html/body/div[1]/div/form/table/tbody/tr[14]/td[2]/input",
    roloverrequirement="/html/body/div[1]/div/form/table/tbody/tr[15]/td[2]/input",
    maxbetlimit="/html/body/div[1]/div/form/table/tbody/tr[16]/td[2]/input",
    usecontributionrate= "/html/body/div[1]/div/form/table/tbody/tr[24]/td[2]/input",
    fordesktopgames = "/html/body/div[1]/div/form/table/tbody/tr[25]/td[2]/input",
    formobilegames = "/html/body/div[1]/div/form/table/tbody/tr[26]/td[2]/input",
    includedplatformcheckall = "/html/body/div[1]/div/form/table/tbody/tr[29]/td[2]/input[1]",
    includedplatformuncheckall = "/html/body/div[1]/div/form/table/tbody/tr[29]/td[2]/input[2]",
    matchbookcheckbox = "/html/body/div[1]/div/form/table/tbody/tr[30]/td[2]/div/table/tbody/tr[1]/td[1]",
    netentcheckbox = "/html/body/div[1]/div/form/table/tbody/tr[30]/td[2]/div/table/tbody/tr[2]/td[1]/input",
    evocheckbox = "/html/body/div[1]/div/form/table/tbody/tr[30]/td[2]/div/table/tbody/tr[3]/td[1]/input",
    redtigerckbox="/html/body/div[1]/div/form/table/tbody/tr[30]/td[2]/div/table/tbody/tr[4]/td[1]/input",
    includegamescheckall="/html/body/div[1]/div/form/table/tbody/tr[31]/td[2]/input[1]",
    includegamesuncheckall="/html/body/div[1]/div/form/table/tbody/tr[31]/td[2]/input[2]",
    openToAll="openToAll",
    includegamesexpand="//*[@id='expand']",
    notes="//*[@id='notes']",
    bonustitle="/html/body/div[1]/div/form/table/tbody/tr[36]/td[2]/input",
    bonusdescription="bonusPlan.bonusCondition",
    bonusdetail="//*[@id='bonusInfo']",
    termandcondition="/html/body/div[1]/div/form/table/tbody/tr[39]/td[2]/div[2]/div[1]",
    termandcondition1="/html/body/div[1]/div/form/table/tbody/tr[39]/td[2]/div[1]/span[3]/button[1]/svg",
    #
    savebutton="/html/body/div[1]/div/form/table/tbody/tr[41]/td[2]/input[1]",
    claimamounthf="bonusPlan.claimAmount",
    success="/html/body/div[1]/div/div/b",
    assignplayerbutton="/html/body/div[1]/div/span/a[3]",

       )
AdminBonusInfoMap =dict(
    coinvalue="bonusPlan.coinValue",
    numberofbetperline="/html/body/div[1]/div/form/table/tbody/tr[22]/td[2]/table/tbody/tr[2]/td[2]/input",
    numberoflines="bonusPlan.numberOfLines",
    rtstake="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select",
    rtstake1="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[1]",
    rtstake2="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[2]",
    rtstake3="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[3]",
    rtstake4="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[4]",
    rtstake5="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[5]",
    rtstake6="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[6]",
    rtstake7="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[7]",
    rtstake8="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[8]",
    rtstake9="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[9]",
    rtstake10="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[10]",
    rtstake11="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[11]",
    rtstake12="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[12]",
    rtstake13="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[13]",
    rtstake14="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[14]",
    rtstake15="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[15]",
    rtstake16="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[16]",
    rtstake17="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[17]",
    rtstake18="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[18]",
    rtstake19="/html/body/div[1]/div/form/table/tbody/tr[21]/td[2]/select/option[19]",

)