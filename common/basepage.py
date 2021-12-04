# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/410:37 下午
@DESC : 
'''
from selenium import webdriver


class BasePage:
    _url = None

    def __init__(self, driver: webdriver):
        if driver is None:
            self.driver = webdriver.Chrome(executable_path="/Users/kongweicheng/utils/selenium/chromedriver")
        else:
            self.driver = driver
            self.driver.implicitly_wait(3)
        if not self._url:
            self.driver.get(self._url)




