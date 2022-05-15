import os

from keywords_core_technology import excel_read
from keywords_core_technology.excel_read import read_sheet

if __name__ == '__main__':
    # 定义测试用例List
    cases = []
    # 获取指定路径下的所有测试用例：用例集中在 data/ 的路径下
    for path, dir, files in os.walk('./data'):
        # 保存获取的所有测试用例文件：其实就是后缀名为xlsx的文件
        for file in files:
            # 获取文件信息
            file_name = os.path.splitext(file)[0]
            file_type = os.path.splitext(file)[1]
            # 判断文件是否为Excel
            if file_type == '.xlsx':
                # 判断是否需要添加该用例
                if 'old' in file_name:
                    pass
                else:
                    cases.append(path + '/' + file)
            else:
                print('文件类型错误：{}'.format(file))
    for case in cases:
        read_sheet.read(case)