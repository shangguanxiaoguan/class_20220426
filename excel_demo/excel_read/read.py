'''
    Excel测试用例的内容读取以及执行的操作行为
'''

import openpyxl


# 获取Excel文件
from excel_demo.keys_excel.ui_keys import Keys

excel = openpyxl.load_workbook('../data/测试数据.xlsx')

# 获取指定的sheet页
sheet = excel['Sheet1']

# 获取sheet页中的所有内容
for values in sheet.values:
    # print(values)
    if type(values[0]) is int:     # 把测试用例的标题排除了
        # print(values)
        print('正在执行：{}'.format(values[5]))
        # 操作过程中关联的测试数据
        data = {}
        data['by'] = values[2]
        data['value'] = values[3]
        data['txt'] = values[4]
        # 把取出的为None的数据清除
        for k in list(data.keys()):
            if data[k] is None:
                del data[k]
        # print('测试数据：{}'.format(data))
        # 操作行为的执行
        # print('测试行为：' + values[1])
        # key = Keys(**data)
        if values[1] == 'open_browser':
            key = Keys(**data)
            print("key--->" + str(key))
        else:
            getattr(key, values[1])(**data)    # 反射机制
        # print('*' * 20)


