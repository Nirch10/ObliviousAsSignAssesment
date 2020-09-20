import json
from random import randrange

from Utils.HttpsConnector import HttpsClient
from Utils.abstractSign import ClientSignatureCreator


class Client(ClientSignatureCreator):
    def __init__(self, key_g_ip: str, key_g_port: int, server_ip: str, server_port: str,
                 certificate_path: str):
        """
        :param key_g_ip: keyGenerator ip - to get clients b, c params for the calculations
        :param key_g_port: port on which @param key_g_ip listens to
        :param server_ip: servers ip the client will try and make connection after calculation
        :param server_port: port on which @param server_ip listens to
        :param certificate_path: certificate file path to verify on each request
        """
        self.key_generator_client = HttpsClient(key_g_ip, key_g_port, certificate_path)
        self.server_client = HttpsClient(server_ip, server_port, certificate_path)
        super(Client, self).__init__()
        self.y_tag = -1;
        self.x = randrange(0, self.p)
        self.b = -1;
        self.c = -1;

    def init_generator_key(self, uri: str) -> None:
        response = self.key_generator_client.get_request(uri)
        json_res = json.loads(response.content)
        self.b = json_res['b']
        self.c = json_res['c']
        print(self.b)
        print(self.c)

    def init_server_public_key(self, uri: str) -> None:
        response = self.server_client.get_request(uri)
        json_response = json.loads(response.content)
        self.y_tag = json_response['key']
        print(self.y_tag)

    def test_server_connection(self, uri: str) -> None:
        key = super(Client, self).sign(self.b, self.c, self.y_tag)
        print(key)
        json_body = {"clientKey": key}
        response = self.server_client.post_request(uri, json_body)
        print(json.loads(response.content))


def start_client():
    k = Client('localhost', 5051, 'localhost', 5000, '/Users/sapirchodorov/git_projects/crt/rootCA.pem')
    k.init_server_public_key('/getKey')
    k.init_generator_key('/getClientKey')
    k.test_server_connection('/testConnection')

