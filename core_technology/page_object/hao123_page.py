from core_technology.base.base_page import BasePage


class Hao123Page(BasePage):
    # URL
    # url = 'https://www.hao123.com/?src=from_pc'
    url = 'https://www.jd.com/'
    # 关键元素
    link = ('link text', 'hao123推荐')

    # 核心业务
    def click_hao(self):
        self.open(self.url)
        self.click(*self.link)
        self.wait(3)
