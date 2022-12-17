import json
import pygal
import math

# 将数据加载到一个列表中
filename = 'data/btc_close_2017-requests.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5 个列表，分别存储日期和收盘价
dates, months, weeks, weekdays, close = [], [], [], [], []

# 每一天的信息
for btc_dict in btc_data:
    # date = btc_dict['date']
    # month = int(btc_dict['month'])
    # week = int(btc_dict['week'])
    # weekday = btc_dict['weekday']
    # close = int(float(btc_dict['close']))
    # print(f"{date} is month {month} week {week}, {weekday}, the close price is {close} RMB.")

    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# x 轴上日期标签顺时针旋转 20°，show_minor_x_labels 是否显示所有 x 轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价（¥）'
line_chart.title = '收盘价对数交换（¥）'
line_chart.x_labels = dates

# x 轴坐标每隔20 天显示一次
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价拆线图（¥）.svg')
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换拆线图（¥）.svg')
