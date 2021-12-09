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
from page.author import AuthorIndex
from page.dashboard import DashboardIndex
from page.view import ViewIndex


class Login(BasePage):  # 登陆类  将登陆功能封装
    _url = 'http://1.117.156.17:8090/admin'

    def login(self):  # 登陆方法
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "用户名/邮箱"]').send_keys("bigllxx@163.com")
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "密码"]').send_keys("123456Zz.")
        self.driver.find_element(By.XPATH, '//span[text()="登 录"]/..').click()  # 定位到上级标签
        return Index(driver=self.driver)


# 分发器，作用：将driver分配给不同的页面
class Index(BasePage):  # 登陆后跳转的页面

    def enter_article(self):
        self.driver.find_element(By.XPATH, '//span/span[text()="文章"]').click()
        time.sleep(1)
        return ArticleIndex(driver=self.driver)

    def enter_author(self):
        self.driver.find_element(By.XPATH, '//span/span[text()="用户"]').click()
        time.sleep(1)
        return AuthorIndex(driver=self.driver)

    def enter_dashboard(self):
        return DashboardIndex(driver=self.driver)

    def enter_view(self):
        self.driver.find_element(By.XPATH, '//span/span[text()="外观"]').click()
        time.sleep(1)
        return ViewIndex(driver=self.driver)
