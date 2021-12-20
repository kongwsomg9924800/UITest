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

import allure
import pytest
from page.index import Login


@allure.feature('文章相关')
class TestArticle:
    # title = 'title  ' + str(uuid.uuid1())

    def setup_class(self):  # 前置条件 定位到"文章"
        self.l = Login().login()

    def teardown_class(self):  # 后置条件 在所有用例执行完毕后关闭浏览器
        time.sleep(3)
        self.l.driver.quit()

    # @pytest.mark.run(order=1)   指定用例执行顺序
    @allure.story('草稿')
    @pytest.mark.parametrize('title, des', [['title  ' + str(uuid.uuid1()), "miao shu"],
                                            ['title  ' + str(uuid.uuid1()), "miao shu 1"]])
    def test_write_caogao(self, title, des):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().caogao(title, des)
        print(res)
        time.sleep(2)

    # @pytest.mark.run(order=2)
    @allure.story('发布')
    def test_write_fabu(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().fabu()
        print(res)

    @allure.story('预览')
    def test_write_yulan(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().yulan('xxx', 'xxx')
        print(res)

    @allure.story('附件库')
    def test_write_fuianku(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res = self.l.enter_article().enter_all_article().fuianku()
        print(res)

    @allure.story('写文章')
    def test_write_article(self):
        # 通过链式调用实现driver的传递，po模式的核心
        res: str = self.l.enter_article().enter_write_article().write_page()
        assert res.split('/')[-1] == 'write'

    # @pytest.mark.parametrize()
    @allure.story('新增种类')
    def test_add_kind(self):
        res = self.l.enter_article().enter_kind_list().add_kind('test2', 'test2', 'test', 'test', 'test')
        assert res == 'test2（加密）'

    @allure.story('编辑种类')
    @pytest.mark.skip()
    def test_update_kind(self):
        res = self.l.enter_article().enter_kind_list().update_kind('test3', 'test3', 'test', 'test', 'test')
        assert res == 'test3（加密）'

