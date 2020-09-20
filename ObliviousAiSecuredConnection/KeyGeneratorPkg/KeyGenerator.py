import os
import requests
from flask import Flask
from ServerPkg.Server import create_response
from Utils.HttpsConnector import HttpsServer, HttpsClient
from Utils.abstractSign import ProxySignatureCreator
import ssl

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


class KeyGenerator(HttpsServer, HttpsClient, ProxySignatureCreator):
    def __init__(self, ip: str, port: int, server_ip: str, server_port: int, certificate_path: str):
        """
        :param ip: ip of this keyGenerator to listen to
        :param port: port on which this keyGenerator will listen to
        :param server_ip: server ip addr to which the generator will send a and params
        :param server_port: port on which the @param server_ip listens to
        :param certificate_path: certificate file path to verify on each request
        """
        super(KeyGenerator, self).__init__(ip, port)
        HttpsClient.__init__(KeyGenerator, server_ip, server_port, certificate_path)
        ProxySignatureCreator.__init__(KeyGenerator)
        self.values_to_gen = super(KeyGenerator, self).sign()
        self.server_port = port
        self.server_ip = ip

    def _setup_server(self) -> int:
        """
        Inits the server's key based on the keygenerator generated data (a, b,c, d)
        :param server_ip: ip of the server to sends params a & d
        :param server_port: port on which servers listens
        :return: status code returned from server
        """

        def _init_json_req():
            return {"key_a": self.values_to_gen['a'], "key_d": self.values_to_gen['d']}

        json_body = _init_json_req();
        res = HttpsClient.post_request(KeyGenerator, '/updateKey', json_body)
        return res.status_code

    def init_proxy(self):
        """
        Initializes server's key and set up keyGenerator as a server in order to let client to get it's credentials
        :param server_ip: server's ip to set key for
        :param server_port: port on which server listens
        """
        code = self._setup_server()
        if code == 200:
            self.serve()

    def get_client_credentials(self) -> dict:
        return {'b': self.values_to_gen['b'], 'c': self.values_to_gen['c']}

    def serve(self):
        app.run(host=self.server_ip, port=self.server_port, debug=True, ssl_context=self.context)


@app.route('/getClientKey')
def get_client_key():
    res = key_generator.get_client_credentials()
    response = create_response(res, 200, 'application/json')
    return response


@app.route('/')
def welcome():
    return 'response'


def start_generator():
    global key_generator
    key_generator = KeyGenerator('127.0.0.1', 5051,'localhost', 5000, '/Users/sapirchodorov/git_projects/crt/rootCA.pem')
    key_generator.init_proxy();
