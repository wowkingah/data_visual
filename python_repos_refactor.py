import requests

from plotly import offline


def get_response():
    """执行 API 调用，并返回响应"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    # GitHub headers
    headers = {'Accept': 'application/vnd.github+json'}
    r = requests.get(url, headers=headers)
    return r


def get_repo_dicts(r):
    """返回一系列表示最受欢迎仓库的字典"""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts


def get_project_data(repo_dicts):
    """提取有关项目的数据，以便用于可视化"""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels


def make_visualization(repo_links, stars, labels):
    """可视化最受欢迎的项目"""
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')


if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)
