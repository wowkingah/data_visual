import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

# 使用 proxies
proxies = {"http": "http://127.0.0.1:7890",
           "https": "http://127.0.0.1:7890"}

req = requests.get(json_url, proxies=proxies)

# 将数据写入文件
with open('data/btc_close_2017-requests.json', 'w') as f:
    f.write(req.text)

# 加载 json 格式
file_requests = req.json()
print(file_requests)
