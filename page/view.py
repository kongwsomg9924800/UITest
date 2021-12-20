# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/110:34 下午
@DESC : 
'''
import time

from selenium.webdriver.common.by import By

from common.basepage import BasePage


class ViewIndex(BasePage):
    log_name = 'ViewIndex'

    def enter_all_view(self):
        self.driver.find_element(By.XPATH, '//a/span[text()="所有页面"]/..').click()
        time.sleep(1)
        return AllView(driver=self.driver)

    def enter_add_view(self):
        self.driver.find_element(By.XPATH, '//a/span[text()="新建页面"]/..').click()
        time.sleep(1)
        return AddView(driver=self.driver)


class AllView(BasePage):
    log_name = 'AllView'

    def manager_link_save(self, name, link, logo, group, index, des):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[0].click()
        self.driver.find_elements(By.CSS_SELECTOR, 'input.ant-input')[0].send_keys(name)
        self.driver.find_elements(By.CSS_SELECTOR, 'input.ant-input')[1].send_keys(link)
        self.driver.find_elements(By.CSS_SELECTOR, 'input.ant-input')[2].send_keys(logo)
        self.driver.find_elements(By.CSS_SELECTOR, 'input.ant-input')[3].send_keys(group)
        self.driver.find_element(By.CSS_SELECTOR, 'input.ant-input-number-input').send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, 'textarea.ant-input').send_keys(des)
        self.driver.find_element(By.CSS_SELECTOR, 'span.ant-form-item-children>button').click()

    def manager_link_edit(self):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[0].click()
        ...

    def manager_link_del(self):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[0].click()
        ...

    def manager_link_check(self):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[0].click()
        ...

    def manager_link_setting(self, name):
        from selenium.webdriver.common.keys import Keys

        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[0].click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary.ant-btn-circle').click()
        self.driver.find_element(By.XPATH, '//div[text()="* 需要主题进行适配"]/../span/input').send_keys(Keys.COMMAND, 'a')
        self.driver.find_element(By.XPATH, '//div[text()="* 需要主题进行适配"]/../span/input').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'div.ant-modal-footer>button').click()

    def manager_img(self):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[1].click()

    def manager_log(self):
        self.driver.find_elements(By.XPATH, '//a[text()="管理"]')[2].click()

    def access(self):
        ...

    def edit(self):
        ...

    def recover(self):
        ...

    def setting(self):
        ...


class AddView(BasePage):
    pass
