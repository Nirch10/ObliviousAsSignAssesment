import json
import ssl
from random import randrange

import requests

from Utils.HttpsConnection import HttpsClient
from Utils.abstractSign import ClientSignatureCreator

ssl._create_default_https_context = ssl._create_unverified_context


class Client(HttpsClient, ClientSignatureCreator):
    def __init__(self, key_generator_ip_port, server_ip_port):

        # super(Client, self).__init__('localhost',5000)
        super(Client, self).__init__()
        self.key_generator_url = ''.join(['https://',key_generator_ip_port])
        self.server_url = ''.join(['https://',server_ip_port])
        self.y_tag = -1;
        self.x = randrange(0,self.p)
        self.b = -1;
        self.c = -1;

    def init_generator_key(self, uri: str) -> None:
        # url = ''.join([self.key_generator_url, uri])
        # res = requests.get(url, verify='/Users/sapirchodorov/git_projects/crt/rootCA.pem')
        # json_res = json.loads(res.content)
        json_res = json.loads()
        self.b = json_res['b']
        self.c = json_res['c']
        print(self.b)
        print(self.c)

    def init_server_public_key(self, uri:str) -> None:
        url = ''.join([self.server_url, uri])
        res = requests.get(url, verify='/Users/sapirchodorov/git_projects/crt/rootCA.pem')
        self.y_tag = json.loads(res.content)['key']
        print(self.y_tag)

    def test_server_connection(self, uri: str) -> None:
        key = super(Client, self).sign(self.b, self.c, self.y_tag)
        print(key)
        json_body = {"clientKey": key}
        url = ''.join([self.server_url, uri])
        res = requests.post(url, json=json_body, verify='/Users/sapirchodorov/git_projects/crt/rootCA.pem')
        print(json.loads(res.content))


def start_client():
    k = Client('localhost:5051', 'localhost:5000')
    k.init_server_public_key('/getKey')
    k.init_generator_key('/getClientKey')
    k.test_server_connection('/testConnection')

