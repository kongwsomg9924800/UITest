# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/410:56 下午
@DESC : 
'''
import time

from selenium.webdriver.common.by import By
from common.basepage import BasePage
from page.article import ArticleIndex


class Login(BasePage):
    _url = 'http://1.117.156.17:8090/admin'

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "用户名/邮箱"]').send_keys("bigllxx@163.com")
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "密码"]').send_keys("123456Zz.")
        self.driver.find_element(By.XPATH, '//span[text()="登 录"]/..').click()  # 定位到上级标签
        return Index(driver=self.driver)


class Index(BasePage):

    def enter_article(self):
        self.driver.find_element(By.XPATH, '//span/span[text()="文章"]').click()
        time.sleep(3)
        return ArticleIndex(driver=self.driver)

    def enter_author(self):
        ...

    def enter_dashboard(self):
        ...

    def enter_view(self):
        ...
