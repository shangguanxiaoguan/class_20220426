# 基类：提供一系列浏览器操作行为，用于在页面对象的实际操作过程中
from time import sleep

from selenium import webdriver


class BasePage:
    # 临时driver定义
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    # 访问URL
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入
    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    # 点击
    def click(self, by, value):
        self.locate(by, value).click()

    # 关闭
    def quit(self):
        self.driver.quit()

    # 等待
    def wait(self, time):
        sleep(time)