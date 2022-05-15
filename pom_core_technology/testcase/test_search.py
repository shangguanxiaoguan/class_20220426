import unittest

# import ddt
import pytest
from ddt import ddt, file_data
from selenium import webdriver

from pom_core_technology.page_object.hao123_page import Hao123Page
from pom_core_technology.page_object.search_page import SearchPage


# @pytest.mark.search
@ddt
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

        # @pytest.mark.search

    @file_data('../data/search.yaml')
    def test_01_search(self, txt):
        print("-----search-----")
        # driver = webdriver.Chrome()
        sp = SearchPage(self.driver)
        sp.search(txt)
        # self.wait(3)

    def test_02_jd(self):
        print("------jd------")
        # driver = webdriver.Chrome()  # 每次都写一次这个，就会导致没执行一个case就会重新打开一个浏览器，这样会导致登录操作无法继续
        hp = Hao123Page(self.driver)
        hp.click_hao()


if __name__ == '__main__':
    # pytest.main(["-s", "test_search.py"])
    unittest.main()

    """
    然后我们已知unittest默认加载脚本的顺序是：根据ASCII码的顺序加载，数字与字母的顺序为：0-9，A-Z，a-z。所以以A开头的测试⽤例
    ⽅法会优先执⾏，以a开头会后执⾏。

    """
