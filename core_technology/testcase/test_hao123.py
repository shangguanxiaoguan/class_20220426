from selenium import webdriver

from core_technology.page_object.hao123_page import Hao123Page
from core_technology.page_object.search_page import SearchPage
import unittest


class TestHao123(unittest.TestCase):
    def test_hao123_link(self):
        driver = webdriver.Chrome()
        sp = SearchPage(driver)
        hp = Hao123Page(driver)
        hp.click_hao()