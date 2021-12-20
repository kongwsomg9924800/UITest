# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/1710:28 下午
@DESC : 
'''
import time
import uuid
import pytest
from page.index import Login


class TestView:
    # title = 'title  ' + str(uuid.uuid1())

    def setup_class(self):  # 前置条件 定位到"文章"
        self.l = Login().login()

    def teardown_class(self):  # 后置条件 在所有用例执行完毕后关闭浏览器
        time.sleep(3)
        self.l.driver.quit()

    def test_manager_link_save(self):
        self.l.enter_view().enter_all_view().manager_link_save('xxx', 'https://www.baidu.com', 'xxxx', 'xxxx', '1', 'xxx')

    def test_manager_link_setting(self):
        self.l.enter_view().enter_all_view().manager_link_setting('友情链接test')
