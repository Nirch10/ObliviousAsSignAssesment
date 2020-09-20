import requests
from requests import Response


class HttpsServer:
    def __init__(self, ip: str, port: int):
        self.server_ip = ip
        self.server_port = port
        self.context = ('/Users/sapirchodorov/git_projects/crt/server.crt',
                   '/Users/sapirchodorov/git_projects/crt/server.key')  # certificate and key files

    def serve(self):
        pass;


class HttpsClient:
    def __init__(self, server_ip: str, server_port: int, cert_path:str):
        self.server_address = ''.join(['https://', server_ip, ':', str(server_port)])
        self.certificate = cert_path

    def get_request(self, uri: str = '/', json_data: str = '') -> Response:
        url = ''.join([self.server_address, self, uri])
        res = requests.get(url, json=json_data, verify=self.certificate)
        return res

    def post_request(self, uri: str, json_data: str):
        url = ''.join([self.server_address, uri])
        res = requests.post(url, json=json_data, verify=self.certificate)
        return res