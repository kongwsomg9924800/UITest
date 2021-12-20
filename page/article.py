# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/110:33 下午
@DESC : 
'''
import logging
import time
import uuid
from common.basepage import BasePage
from selenium.webdriver.common.by import By


class ArticleIndex(BasePage):
    log_name = 'ArticleIndex'

    def enter_all_article(self):
        
        self.find(By.XPATH, '//span[text()="所有文章"]/..').click()
        return AllArticle(driver=self.driver)

    def enter_write_article(self):
        self.find(By.XPATH, '//span[text()="写文章"]/..').click()
        return WriteArticle(driver=self.driver)

    def enter_kind_list(self):
        self.find(By.XPATH, '//span[text()="分类目录"]/..').click()
        return KindList(driver=self.driver)

    def enter_tag(self):
        self.find(By.XPATH, '//span[text()="标签"]/..').click()
        return Tag(driver=self.driver)


class AllArticle(BasePage):
    log_name = 'AllArticle'
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

    def write_article(self, title=None, des=None):
        
        self.finds(By.CSS_SELECTOR, self.local_attr['写文章'])[1].click()
        
        # 先写标题，在写描述
        self.find(By.CSS_SELECTOR, self.local_attr['文章标题']).send_keys(title)
        self.find(By.CSS_SELECTOR, self.local_attr['文章描述']).send_keys(des)
        return self.driver

    def caogao(self, title, des):
        self.write_article(title, des)
        self.find(By.XPATH, self.local_attr['保存草稿']).click()

    def yulan(self, title, des):
        self.write_article(title, des)
        self.find(By.XPATH, self.local_attr['预览']).click()
        
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换浏览器标签页到第一个

    def fabu(self, title, des):
        self.write_article(title, des)
        self.find(By.XPATH, self.local_attr['发布']).click()
        self.finds(By.CSS_SELECTOR, self.local_attr['标签'])[0].click()
        self.finds(By.XPATH, self.local_attr['保存草稿'])[1].click()

    def fuianku(self, title='', des=''):
        self.write_article(title, des)
        self.find(By.XPATH, self.local_attr['附件库']).click()

    def del_article(self):
        a = self.finds(By.XPATH, '//a[text()="删除"]')
        b = self.finds(By.XPATH, '//a[text()="回收站"]')
        while len(a) != 0 or len(b) != 0:
            if len(a) == 0:
                self.finds(By.XPATH, '//a[text()="回收站"]')[0].click()
                
                self.find(By.XPATH, '//span[text()="确 定"]/..').click()
                
            else:
                self.finds(By.XPATH, '//a[text()="删除"]')[0].click()
                
                self.find(By.XPATH, '//span[text()="确 定"]/..').click()
                
            b = self.finds(By.XPATH, '//a[text()="回收站"]')
            a = self.finds(By.XPATH, '//a[text()="删除"]')
            self.driver.refresh()
            


class WriteArticle(BasePage):

    def write_page(self):
        
        url = self.driver.current_url
        return url


class KindList(BasePage):

    def add_kind(self, name, fake_name, img_url, password, des):
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[0].send_keys(name)
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[1].send_keys(fake_name)
        self.find(By.CSS_SELECTOR, 'span.ant-select-selection__rendered').click()
        
        self.finds(By.CSS_SELECTOR, 'span.ant-select-tree-title')[0].click()
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[2].send_keys(img_url)
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[3].send_keys(password)
        self.find(By.CSS_SELECTOR, 'textarea.ant-input').send_keys(des)
        self.find(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary').click()
        self.driver.refresh()
        
        res = self.finds(By.CSS_SELECTOR, 'span.cursor-pointer')[0].text
        return res

    def update_kind(self, name, fake_name, img_url, password, des):
        self.finds(By.CSS_SELECTOR, "tr.ant-table-row.ant-table-row-level-0>td>span>a")[0].click()
        a = self.finds(By.CSS_SELECTOR, 'input.ant-input')[0]
        # print('=======================')
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[0].send_keys(name)
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[1].send_keys(fake_name)
        self.find(By.CSS_SELECTOR, 'span.ant-select-selection__rendered').click()
        
        self.finds(By.CSS_SELECTOR, 'span.ant-select-tree-title')[0].click()
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[2].send_keys(img_url)
        self.finds(By.CSS_SELECTOR, 'input.ant-input')[3].send_keys(password)
        self.find(By.CSS_SELECTOR, 'textarea.ant-input').send_keys(des)
        self.find(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary').click()
        self.driver.refresh()
        
        res = self.finds(By.CSS_SELECTOR, 'span.cursor-pointer')[0].text
        return res


class Tag(BasePage):
    ...
