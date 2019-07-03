'''
Created on Feb06 , 2019

@author: Daryoush
'''
Admin_Constants = dict(Browser           = "chrome",
                        Base_URL          = "http:/dev06.xcl.ie:20194/zf/login",
                        Client_URL          = "https://dev06.xcl.ie/casino",
                        # Client_URL          = "https://www.matchbook.com",
                        #Base_URL          = "http://192.168.1.133:8000",  #Red env
                        #Base_URL="http://10.68.0.237:8000",  # Red second env
                        Admin_Username = "dtahouri",
                        Admin_Password = "Password1"

                        )
Admin_Dynamic = dict(
                        globalname="Djune19_",#Based on this name users created, bonus created, bonus assigned
                        uipassword="Password1",
                        createallbonuses="1",#zero mean no crealtion of all bonuses
                        createallusers="1",#zero mean no crealtion of all users
                        CasinoClassicRedDogGameLink="https://dev06.xcl.ie/casino/play/PL49/T0012?limit=0"

                       )


class LocatorMode:
 
 ID           = "id"
 NAME         = "name"
 XPATH        = "xpath"
 CSS_SELECTOR = "cssSelector"
