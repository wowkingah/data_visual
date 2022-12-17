from __future__ import (absolute_import, division, print_function, unicode_literals)

import urllib.request
import json

try:
    # Python 2.x
    from urllib2 import urlopen
except ImportError:
    # Python 3.x
    from urllib.request import urlopen

proxy_support = urllib.request.ProxyHandler({'http': '127.0.0.1:7890',
                                             'https': '127.0.0.1:7890'})
# 定制安装 opener
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)

# 读取数据
req = response.read()

# 将数据写入文件
with open('data/btc_close_2017-urllib.json', 'wb') as f:
    f.write(req)

# 加载 json 格式
file_urllib = json.loads(req)
print(file_urllib)
