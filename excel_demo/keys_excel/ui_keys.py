'''
    关键字驱动底层
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
    python反射机制：
        四大内置函数：常用的是其中的getattr函数，就是获取指定类的指定属性
        getattr（类，属性）  相当于 类.属性 的意思
        例如：
            webdriver.Chrome == getattr(webdriver, 'Chrome')
        基于反射获取属性是这个反射函数的基本定义，获取函数就需要在末尾加上()
        例如： open_browser()函数：
            不用反射的形态：
                if type_ == Chrome:
                    driver = webdriver.Chrome()
                elif type_ == Firefox:
                    driver = webdriver.FireFox()
                elif type_ == Ie:
                    driver = webdriver.Ie()
                elif safari
                elif edge
'''


# 构造一个浏览器对象
def open_browser(txt):
    try:
        driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Keys:
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, txt):
        self.driver = open_browser(txt)
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
