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
        self.driver = webdriver.Chrome(executable_path="/Users/kongweicheng/utils/selenium/chromedriver")  # driver是浏览器进程
        self.driver.get("http://1.117.156.17:8090/admin")

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    def setup(self):  # 登陆 所有页面都是登陆之后才能进入
        # input[placeholder = "用户名/邮箱"]
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "用户名/邮箱"]').send_keys("bigllxx@163.com")

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder = "密码"]').send_keys("123456Zz.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//span[text()="登 录"]/..').click()  # 定位到上级标签
        time.sleep(3)  # 登陆动作需要时间
        assert self.driver.current_url == "http://1.117.156.17:8090/admin/index.html#/dashboard"

    def test_dashboard_general(self):
        a = self.driver.find_elements(By.CSS_SELECTOR, "div.ant-card")
        assert len(a) == 7

    def test_dashboard_write(self):
        self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="写点什么吧..."]').send_keys('slkfnadksbfk328yr9832hnrfkndskjahfiuy23rrghsbfcjkdbsvfjgads')
        self.driver.find_element(By.XPATH, '//span[text()="发 布"]/..').click()


