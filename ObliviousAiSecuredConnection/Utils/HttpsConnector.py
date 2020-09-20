import os
import ssl

import requests
from requests import Response


class HttpsServer:
    ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, ip: str, port: int, cert_path: str, cert_key_path: str):
        """

        :param ip: ip of this HttpsServer to listen to
        :param port: port on which this HttpsServer will listen to
        :param cert_path: keyGenerator server valid certificate file path
        :param cert_key_path: keyGenerator server valid certificate key file path
        """
        self.server_ip = ip
        self.server_port = port
        self.context = (cert_path, cert_key_path)  # certificate and key files

    def serve(self):
        pass;


class HttpsClient:
    ssl._create_default_https_context = ssl._create_unverified_context

    def __init__(self, server_ip: str, server_port: int, cert_path: str):
        self.server_address = ''.join(['https://', server_ip, ':', str(server_port)])
        self.certificate = cert_path

    def get_request(self, uri: str = '/', json_data: str = '') -> Response:
        url = ''.join([self.server_address, uri])
        res = requests.get(url, json=json_data, verify=self.certificate)
        return res

    def post_request(self, uri: str, json_data: str):
        url = ''.join([self.server_address, uri])
        res = requests.post(url, json=json_data, verify=self.certificate)
        return res
