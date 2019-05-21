'''
Created on Feb06 , 2019

@author: Daryoush
'''
Admin_Constants = dict(Browser           = "firefox",
                        Base_URL          = "http:/dev06.xcl.ie:20194/zf/login",
                        Client_URL          = "https://dev06.xcl.ie/casino",
                        #Base_URL          = "https://www.matchbook.com",
                        #Base_URL          = "http://192.168.1.133:8000",  #Red env
                        #Base_URL="http://10.68.0.237:8000",  # Red second env
                        Admin_Username = "dtahouri",
                        Admin_Password = "Password1"
                        )

class LocatorMode:
 
 ID           = "id"
 NAME         = "name"
 XPATH        = "xpath"
 CSS_SELECTOR = "cssSelector"
