# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/410:37 下午
@DESC : 
'''
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logs import Logger


class BasePage:  # 所有页面类的父类
    _url = None
    log_name = None
    logs = Logger('Base')

    def __init__(self, driver=None):
        if driver is None:  # 如果没有driver进程，打开浏览器，并指定Chromedriver版本
            self.driver = webdriver.Chrome(executable_path="/Users/kongweicheng/utils/selenium/chromedriver")
        else:
            self.driver = driver
            self.driver.implicitly_wait(3)
        if self._url:
            self.driver.get(self._url)

    def find(self, by=By.CSS_SELECTOR, location=None):  # 隐藏driver
        # 1.精简代码 2.隐藏driver 3.日志输出 4.显式等待
        el = (by, location)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(el))
        except:
            self.logs.logger.error('{} - 定位失败：{}'.format(self.log_name, location))
            return None
        else:
            self.logs.logger.info('{} - 定位成功：{}'.format(self.log_name, location))
            return self.driver.find_element(by, location)

    def finds(self, by=By.CSS_SELECTOR, location=None):
        el = (by, location)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(el))
        except:
            self.logs.logger.error('{} - 定位失败：{}'.format(self.log_name, location))
            return None
        else:
            self.logs.logger.info('{} - 定位成功：{}'.format(self.log_name, location))
            return self.driver.find_elements(by, location)
