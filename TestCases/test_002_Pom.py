import time
from  Bese import InitiateDriver
from selenium.webdriver import Chrome
from Library import ConfigReder
from Pages import Registation
import pytest
def data_driven():
    li=[['user1','pass1'],['user2','pass2'],['user3','pass3']]
    return li

@pytest.mark.parametrize('data',data_driven())
def test_registation(data):
    driver=InitiateDriver.startbroswer()
    registation=Registation.Registion(driver)
    registation.enter_username(data[0])
    registation.enter_email(data[1])
    #registation.enter_phoneno()