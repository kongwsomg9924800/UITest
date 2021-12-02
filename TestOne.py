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
        self.driver.get("http://1.117.156.17:8090/admin")

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        # input[placeholder = "用户名/邮箱"]
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "用户名/邮箱"]').send_keys("bigllxx@163.com")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "密码"]').send_keys("123456Zz.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//span[text()="登 录"]/..').click()  # 定位到上级标签

