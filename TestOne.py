# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/110:09 下午
@DESC : 
'''
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestOne:

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path="/Users/kongweicheng/utils/selenium/chromedriver")
        self.driver.get("https://www.baidu.com")

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, 'kw').send_keys("python")
        time.sleep(2)
        self.driver.find_element(By.ID, 'su').click()

