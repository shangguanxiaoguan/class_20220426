from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
  从selenium库中，将常用的操作行为进行提取，封装成关键字类
'''


# 构造浏览器对象：调用python的反射机制
def open_browser(txt):
    try:
        driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Keys:
    # driver = webdriver.Chrome()

    # 构造函数，用于构造初始化的浏览器对象
    def __init__(self, type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(5)

    # 访问URL
    def open(self, txt):
        self.driver.get(txt)

    # 元素定位
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 点击
    def click(self, by, value):
        self.locate(by, value).click()

    # 输入
    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    # 强制等待
    def wait(self, txt):
        sleep(txt)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda  el: self.locate(name, value), message='元素查找失败')

    # 句柄的切换
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败
    def assert_text(self, by, value, expect):
        try:
            reality = self.locate(by, value).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('出现异常，断言失败')
