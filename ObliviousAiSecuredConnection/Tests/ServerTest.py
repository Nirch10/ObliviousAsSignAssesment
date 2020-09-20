import unittest

import requests

from ServerPkg.Server import Server


class ServerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_running(self):
        self.assertEqual(requests.get('https://localhost:1235', verify='/Users/sapirchodorov/git_projects/crt/rootCA'
                                                                       '.pem').status_code, 200)

    def test_get_public_key(self):
        self.assertEqual(requests.get('https://localhost:1235/getKey', verify='/Users/sapirchodorov/git_projects/crt/rootCA'
                                                                       '.pem').status_code, 200)

    def test_bypass_generator(self):
        self.assertEqual(
            requests.post('https://localhost:1235/testConnection',json= {"clientKey": -1}, verify='/Users/sapirchodorov/git_projects/crt/rootCA.pem').status_code, True)


if __name__ == '__main__':
    unittest.main()
