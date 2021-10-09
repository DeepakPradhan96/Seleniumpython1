import configparser
from Library import  ConfigReder
class Registion():

    def __init__(self,obj):
        global driver
        driver=obj


    #def click_login(self):
       #driver.find_element_by_css_selector(ConfigReder.readConfigdata1('locator', 'Register')).click()

    def enter_username(self,username):
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator', 'name')).send_keys(username)

    def enter_email(self,enter_email):
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator', 'email')).send_keys(enter_email)

    def enter_phoneno(self):
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator','phone')).send_keys('78558666')

