# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/110:33 下午
@DESC : 
'''
import time

from common.basepage import BasePage
from selenium.webdriver.common.by import By


class ArticleIndex(BasePage):
    def enter_all_article(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//span[text()="所有文章"]/..').click()
        return AllArticle(driver=self.driver)

    def enter_write_article(self):
        self.driver.find_element(By.XPATH, '//span[text()="写文章"]/..').click()
        return WriteArticle(driver=self.driver)

    def enter_kind_list(self):
        self.driver.find_element(By.XPATH, '//span[text()="分类目录"]/..').click()
        return KindList(driver=self.driver)

    def enter_tag(self):
        self.driver.find_element(By.XPATH, '//span[text()="标签"]/..').click()
        return Tag(driver=self.driver)


class AllArticle(BasePage):

    def write_article(self):
        self.driver.find_elements(By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary")[1].click()
        time.sleep(2)
        return self.driver.current_url

    def check_1(self):
        ...

    def check_2(self):
        ...

    def check_3(self):
        ...

    def add(self):
        ...


class WriteArticle(BasePage):
    ...


class KindList(BasePage):
    ...


class Tag(BasePage):
    ...

