# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/12/411:33 下午
@DESC : 
'''
from page.index import Login


class TestTwo:
    def setup_class(self):
        self.l = Login().login().enter_article()

    def teardown_class(self):
        self.l.driver.quit()

    def test_all_article(self):
        self.l.enter_all_article()

    def test_write_article(self):
        res = self.l.enter_all_article().write_article()
        print(res)
        assert res == "http://1.117.156.17:8090/admin/index.html#/posts/write"