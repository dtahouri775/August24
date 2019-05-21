from selenium import webdriver

import unittest

from Constants import Exchange_Constants
#from  Constants import TT_Constants


class BaseTestCase(object):

    def setUp(self):
      if Exchange_Constants['Browser'].lower() == "firefox":
      	 self.driver = webdriver.Firefox()
      elif Exchange_Constants['Browser'].lower() == "chrome":
      	 self.driver = webdriver.Chrome()
      elif Exchange_Constants['Browser'].lower() == "safari":
         self.driver = webdriver.Safari()
      elif Exchange_Constants['Browser'].lower() == "edge":
         self.driver = webdriver.Edge()
      else:
      	raise Exception("This browser is not supported at the moment.")

    def navigate_to_page(self, url):
      try:
          self.driver.get(url)
      except:   
          raise Exception("The main Dev06 page is not available.")
      

    def tearDown(self):
  	  self.driver.quit()
