import yaml

file = open('../data/list.yaml', 'r', encoding='utf-8')
# 读取Yaml文件中的内容
values = yaml.load(stream=file, Loader=yaml.FullLoader)
print(values)
print(type(values))


file = open('../data/dict.yaml', 'r', encoding='utf-8')
# 读取Yaml文件中的内容
values = yaml.load(stream=file, Loader=yaml.FullLoader)
print(values)
print(type(values))

file = open('../data/data3.yaml', 'r', encoding='utf-8')
# 读取Yaml文件中的内容
values = yaml.load(stream=file, Loader=yaml.FullLoader)
print(values)
print(type(values))

file = open('../data/data4.yaml', 'r', encoding='utf-8')
# 读取Yaml文件中的内容
values = yaml.load(stream=file, Loader=yaml.FullLoader)
print(values)
print(type(values))
