from keywords_core_technology.web_keys.keywords import Keys

key = Keys("Chrome")
key.open('http://www.baidu.com')
key.input('id', 'kw', 'python')
key.click('id', 'kw')
