import unittest

# import ddt
import pytest
from ddt import ddt, file_data
from selenium import webdriver

from core_technology.page_object.hao123_page import Hao123Page
from core_technology.page_object.search_page import SearchPage


# @pytest.mark.search
@ddt
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    # @pytest.mark.search
    @file_data('../data/search.yaml')
    def test_search(self, txt):
        # driver = webdriver.Chrome()
        sp = SearchPage(self.driver)
        sp.search(txt)

        # self.wait(3)

    def test_jd(self):
        # driver = webdriver.Chrome()  # 每次都写一次这个，就会导致没执行一个case就会重新打开一个浏览器，这样会导致登录操作无法继续
        hp = Hao123Page(self.driver)
        hp.click_hao()

if __name__ == '__main__':
    # pytest.main(["-s", "test_search.py"])
    unittest.main()
