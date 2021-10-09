
from selenium.webdriver import Chrome
from Library import ConfigReder
from selenium.webdriver import Firefox
import pytest
#@pytest.fixture()
def startbroswer():
        global driver

        if (ConfigReder.readConfigdata("section1",'Broswer')=='Chorme'):
                driver = Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')

        elif (ConfigReder.readConfigdata("section1",'Broswer')== 'Firefox'):
                driver = Firefox(executable_path='C:\Driver\geckodriver-v0.29.1-win64\geckodriver.exe')

        else:

                driver = Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')


        driver.get(ConfigReder.readConfigdata("section1","Application_url"))
        driver.maximize_window()
        return driver



def closebroswer(startbroswer):
    driver.close()