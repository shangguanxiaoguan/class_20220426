import unittest
from ddt import ddt, file_data

from interface_demo.api_key.keys import Key

@ddt
class TestApiDemo(unittest.TestCase):
    keys = Key()

    @file_data('../data/login.yaml')
    def test_01_api(self, **kwargs):
        res = self.keys.do_post(url=kwargs['url'], json=kwargs['data'])
        print(res.text)
        # self.assertEqual(kwargs['expected'], res.json()['msg'], msg='断言失败，两者不想扽')
        self.assertEqual(kwargs['expected'], self.keys.get_text(res.text, 'msg'), msg='断言失败，两者不想扽')


if __name__ == '__main__':
    unittest.main()
