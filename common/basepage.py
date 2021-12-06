# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/410:37 下午
@DESC : 
'''
from selenium import webdriver


class BasePage:  # 所有页面类的父类
    _url = None

    def __init__(self, driver: webdriver = None):
        if driver is None:  # 如果没有driver进程，打开浏览器，并指定Chromedriver版本
            self.driver = webdriver.Chrome(executable_path="/Users/kongweicheng/utils/selenium/chromedriver")
        else:
            self.driver = driver
            self.driver.implicitly_wait(3)
        if self._url:
            self.driver.get(self._url)




