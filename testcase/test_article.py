# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/411:33 下午
@DESC : 
'''
import time
import uuid

import pytest

from page.article import AllArticle
from page.index import Login


class TestArticle:
    # title = 'title  ' + str(uuid.uuid1())

    def setup_class(self):  # 前置条件 定位到"文章"
        self.l = Login().login()

    def teardown_class(self):  # 后置条件 在所有用例执行完毕后关闭浏览器
        time.sleep(3)
        self.l.driver.quit()

    # @pytest.mark.run(order=1)   指定用例执行顺序
    @pytest.mark.parametrize('title, des', [['title  ' + str(uuid.uuid1()), "miao shu"], ['title  ' + str(uuid.uuid1()), "miao shu 1"]])
    def test_write_caogao(self, title, des):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().caogao(title, des)
        print(res)
        time.sleep(2)

    # @pytest.mark.run(order=2)
    def test_write_fabu(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().fabu()
        print(res)

    def test_write_yulan(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().yulan()
        print(res)

    def test_write_fuianku(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().fuianku()
        print(res)
