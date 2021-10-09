
import time
from  Bese import InitiateDriver
from selenium.webdriver import Chrome
from Library import ConfigReder
def test_login():
        global driver
        driver=InitiateDriver.startbroswer()
        driver.find_element_by_xpath("//label[text()='Login']").click()
        driver.find_element_by_name("_txtUserName").send_keys('test')
        driver.find_element_by_name('_txtPassword').send_keys('test')


# use Config file as locator
'''def test_registation():
        driver.find_element_by_css_selector(ConfigReder.readConfigdata1('locator','Register')).click()
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator','name')).send_keys('Deepak')
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator','email')).send_keys('deepak@gmail.com')
        driver.find_element_by_name(ConfigReder.readConfigdata1('locator','phone')).send_keys('78558666')
        time.sleep(5)
        driver.close()'''
