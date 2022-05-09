from selenium import webdriver

from core_technology.base.base_page import BasePage
from core_technology.page_object.hao123_page import Hao123Page

"""
    函数调用时使用*和 ** ：
        def test(a, b, c)
            test(*args) :* 的作用其实就是把序列args中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3) ，那么这个代码就等价于 test(1, 2, 3) 。
            test(**kwargs)：** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，如果 kwargs 等于 {‘a’:1,’b’:2,’c’:3} ，那这个代码就等价于 test(a=1,b=2,c=3) 。

    函数定义时使用*和** ：
        def test(*args): 
            *args 表示把传进来的位置参数都装在元组 args 里面。比如说上面这个函数，传参调用test(1, 2, 3)的话， args 的值就是 (1, 2, 3) 。
        def test(**kwargs): 
            ** 就是针对关键字参数和字典的了。 传参调用 test(a=1,b=2,c=3)的话， kwargs 的值就是 {'a':1,'b':2,'c':3} 了。
"""


class SearchPage(BasePage):
    # url
    url = 'http://www.baidu.com'

    # 关键元素
    input_el = ('id', 'kw')
    button_el = ('id', 'su')

    # 页面的业务
    def search(self, txt):
        self.open(self.url)
        self.input(*self.input_el, txt)
        self.wait(3)
        # print("----开始点击-----")
        self.click(*self.button_el)
        # print('----点击结束-----')
        self.wait(5)
        # self.quit()



if __name__ == '__main__':
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.search("python")
