import os
from urllib import parse

from flask import Flask

from SignatureGenerator.abstractSign import ProxySignatureCreator
import urllib.request
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


class KeyGenerator(ProxySignatureCreator):
    def __init__(self, ip: str, port: int):
        super(KeyGenerator, self).__init__()
        self.values_to_gen = super(KeyGenerator, self).sign()
        self.server_port = port
        self.server_ip = ip

    def _setup_server(self, server_ip: str, server_port: str) -> int:
        """
        Inits the server's key based on the keygenerator generated data (a, b,c, d)
        :param server_ip: ip of the server to sends params a & d
        :param server_port: port on which servers listens
        :return: status code returned from server
        """
        def _init_json_req():
            return {"key_a": self.values_to_gen['a'], "key_d": self.values_to_gen['d']}

        json_body = _init_json_req();
        url = ''.join(['https://', server_ip, ':', server_port, '/updateKey'])
        res = requests.post(url, json=json_body, verify='/Users/sapirchodorov/git_projects/crt/rootCA.pem')
        return res.status_code

    def init_proxy(self, server_ip: str, server_port: str):
        """
        Initializes server's key and set up keyGenerator as a server in order to let client to get it's credentials
        :param server_ip: server's ip to set key for
        :param server_port: port on which server listens
        """
        code = self._setup_server(server_ip, server_port)
        if code == 200:
            self.serve()
            print('proxy\'s up')

    def get_client_credentials(self) -> dict:
        return {'b': self.values_to_gen['b'], 'c': self.values_to_gen['c']}

    def serve(self):
        context = ('/Users/sapirchodorov/git_projects/crt/server.crt',
                   '/Users/sapirchodorov/git_projects/crt/server.key')  # certificate and key files
        app.run(host=self.server_ip, port=self.server_port, debug=True, ssl_context=context)


if __name__ == '__main__':
    k = KeyGenerator('localhost', 9090)
    k.init_server_key('localhost', '5000');
