import unittest

import python_repos_refactor as pr


class PythonReposTestCase(unittest.TestCase):
    """测试 python_repos.py"""

    def setUp(self):
        """调用所有的函数，并分别测试各个方面"""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = pr.get_project_data(self.repo_dicts)

    def test_get_response(self):
        """测试获得了有效响应"""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """测试获得了期望的数据"""
        # 应获得 30 个描述仓库的字典
        self.assertEqual(len(self.repo_dicts), 30)

        # 描述仓库的字典应包含必要的键
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()
