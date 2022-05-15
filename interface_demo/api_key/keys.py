'''
 关键字驱动：也就是函数的调用，即面向对象编程思维

'''
import json
import jsonpath

import requests


class Key:
    # get
    def do_get(self, url, params=None, headers=None, **kwargs):
        requests.get(url=url, params=params, headers=headers, **kwargs)

    # post
    def do_post(self, url, data=None, headers=None, **kwargs):
        requests.post(url=url, data=data, headers=headers, **kwargs)

    # get_text
    def get_text(self, txt, key):
        '''
        提取响应结果中的某个值
        :param txt: 获取的响应结果
        :param key: 要找的需要断言的key
        :return:
        '''
        try:
            # 把响应结果转换成 json 格式
            txt = json.loads(txt)
            value = jsonpath.jsonpath(txt, '$..{}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
            return value
        except:
            return None
