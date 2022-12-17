import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API 响应存储在一个变量中
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print(f"\nName: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
# 隐藏水平线
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, my_style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
