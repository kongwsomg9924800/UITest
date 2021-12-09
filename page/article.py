# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/110:33 下午
@DESC : 
'''
import time
import uuid
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
    # 所有文章页面，下面一个方法对应一个功能
    local_attr = {
        '写文章': 'button.ant-btn.ant-btn-primary',
        '文章标题': 'input[placeholder="请输入文章标题"]',
        '文章描述': 'textarea[placeholder="开始编辑..."]',
        '保存草稿': '//span[text()="保存草稿"]/..',
        '预览': '//span[text()="预 览"]/..',
        '发布': '//span[text()="发 布"]/..',
        '标签': 'span.ant-tree-checkbox-inner',
        '附件库': '//span[text()="附件库"]/..',
    }

    def write_article(self, title, des):
        time.sleep(2)
        self.driver.find_elements(By.CSS_SELECTOR, self.local_attr['写文章'])[1].click()
        time.sleep(2)
        # 先写标题，在写描述
        self.driver.find_element(By.CSS_SELECTOR, self.local_attr['文章标题']).send_keys(title)
        self.driver.find_element(By.CSS_SELECTOR, self.local_attr['文章描述']).send_keys(des)
        return self.driver

    def caogao(self, title, des):
        self.write_article(title, des)
        self.driver.find_element(By.XPATH, self.local_attr['保存草稿']).click()

    def yulan(self, title, des):
        self.write_article(title, des)
        self.driver.find_element(By.XPATH, self.local_attr['预览']).click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换浏览器标签页到第一个
        time.sleep(2)

    def fabu(self, title, des):
        self.write_article(title, des)
        self.driver.find_element(By.XPATH, self.local_attr['发布']).click()
        self.driver.find_elements(By.CSS_SELECTOR, self.local_attr['标签'])[0].click()
        self.driver.find_elements(By.XPATH, self.local_attr['保存草稿'])[1].click()

    def fuianku(self, title, des):
        self.write_article(title, des)
        self.driver.find_element(By.XPATH, self.local_attr['附件库']).click()

    def del_article(self):
        try:
            for i in range(10):
                if self.driver.find_elements(By.XPATH, '//a[text()="删除"]')[0]:
                    ...
                elif:
                    ...

                self.driver.find_elements(By.XPATH, '//a[text()="回收站"]')[i].click()
                self.driver.find_elements(By.XPATH, '//span[text()="确 定"]/..')[1].click()
                self.driver.find_element()
        except:
            print('======')


class WriteArticle(BasePage):
    ...


class KindList(BasePage):
    ...


class Tag(BasePage):
    ...
