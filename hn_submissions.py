import requests
import pygal

from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API 调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
# Top 30
for submission_id in submission_ids[:30]:
    # 对每篇文章都执行API 调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        # descendants 评论数不存在，返回0
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# 根据评论数排序
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['link']}")
#     print(f"Comments: {submission_dict['comments']}")

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])

    plot_dict = {
        "value": submission_dict['comments'],
        "label": submission_dict['title'],
        "xlink": submission_dict['link']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Comments of Hacker-News"
chart.x_labels = titles
chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')
