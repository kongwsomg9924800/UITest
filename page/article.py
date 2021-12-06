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

    def textarea(self):
        self.driver.find_element(By.XPATH, '//textarea[@placeholder="写点什么吧..."]').send_keys("###########3")
        time.sleep(3)

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

    def write_article_1(self):
        time.sleep(2)
        self.driver.find_elements(By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary")[1].click()
        time.sleep(2)
        # 先写标题，在写描述
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入文章标题"]').send_keys("zhe222222 shi 2222333wen 21 zhang 3 2 title 1")
        self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="开始编辑..."]').send_keys("zhe shi wen zhang des")
        return self.driver

    def caogao(self):
        self.write_article_1()
        self.driver.find_element(By.XPATH, '//span[text()="保存草稿"]/..').click()

    def yulan(self):
        self.write_article_1()
        self.driver.find_element(By.XPATH, '//span[text()="预 览"]/..').click()

    def fabu(self):
        self.write_article_1()
        self.driver.find_element(By.XPATH, '//span[text()="发 布"]/..').click()

    def fuianku(self):
        self.write_article_1()
        self.driver.find_element(By.XPATH, '//span[text()="附件库"]/..').click()


    def write_article_2(self):
        # 先写描述，在写标题
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

