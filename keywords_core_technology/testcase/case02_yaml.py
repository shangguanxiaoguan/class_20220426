from keywords_core_technology.web_keys.keywords import Keys
import unittest
from ddt import ddt, file_data


@ddt
class TestCase(unittest.TestCase):
    @file_data('../data/data.yaml')
    def test_01(self, **kwargs):
        key = Keys(kwargs['type'])
        key.open(kwargs['url'])
        # key.input('id', 'kw', 'python')
        # key.input(**kwargs['input']) 会报错。TypeError: input() got an unexpected keyword argument 'name'
        key.input(kwargs['input']['name'], kwargs['input']['value'], kwargs['input']['txt'])
        key.click(kwargs['click']['name'], kwargs['click']['value'])
        key.wait(kwargs['wait'])
        key.quit()


if __name__ == '__main__':
    unittest.main()
