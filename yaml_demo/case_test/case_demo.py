import unittest
from time import sleep

from selenium import webdriver
from ddt import ddt, file_data


@ddt
class Case(unittest.TestCase):
    # @file_data('../data/url.yaml')
    # def test01(self, url, txt):
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     driver.find_element('id', 'kw').send_keys(txt)
    #     driver.find_element('id', 'su').click()
    #     sleep(3)
    #     driver.quit()

    # @file_data('../data/url.yaml')
    # def test01(self, **kwargs):
    #     driver = webdriver.Chrome()
    #     driver.get(kwargs['url'])
    #     driver.find_element(kwargs['input']['by'], kwargs['input']['value']).send_keys(kwargs['input']['txt'])
    #     driver.find_element(kwargs['button']['by'], kwargs['button']['value']).click()
    #     sleep(3)
    #     driver.quit()

    # @file_data('../data/url.yaml')
    # def test01(self, **kwargs):
    #     driver = webdriver.Chrome()
    #     driver.get(kwargs['url'])
    #     driver.find_element(**kwargs['input']).send_keys(kwargs['txt'])
    #     driver.find_element(**kwargs['button']).click()
    #     sleep(3)
    #     driver.quit()

    @file_data('../data/url.yaml')
    def test01(self, **kwargs):
        # 当网页打开很慢时，加上下面两行代码会变快 selenium的三种页面加载策略
        option = webdriver.ChromeOptions()
        option.page_load_strategy = 'none'
        common = kwargs['common']
        driver = webdriver.Chrome(options=option)  # 注意这里的参数
        # 隐式等待
        driver.implicitly_wait(2)
        driver.get(common['url'])
        driver.find_element(**common['input']).send_keys(kwargs['txt'])
        driver.find_element(**common['button']).click()
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
