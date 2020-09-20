from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify, request, Response
import ssl
import os

# class Server:
#     context = ssl.create_default_context()
#     server_address = ('localhost', 4443)
#     httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
#     httpd.socket = ssl.wrap_socket(httpd.socket,
#                                    server_side=True,
#                                    certfile='localhost.pem',
#                                    ssl_version=ssl.PROTOCOL_TLS)
#     httpd.serve_forever()
#
from SignatureGenerator.abstractSign import ServerSignatureCreator

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


class Server(ServerSignatureCreator):

    def __init__(self, ip: str, port: int):
        super(Server, self).__init__()
        super(Server, self).set_p(11)
        self.server_port = port
        self.server_ip = ip
        self.y_tag = -1

    @staticmethod
    @app.route('/')
    def welcome() -> object:
        return Response(jsonify({"Welcome to my server": 'ss'}), status=200, mimetype='application/json')

    def update_key(self, a: int, d: int) -> int:
        self.y_tag = super(Server, self).sign(a, d)
        return self.y_tag

    def get_key_tag(self) -> int:
        return self.y_tag

    def test_connection(self, predicted_key) -> bool:
        return predicted_key == self.d

    def serve(self):
        context = ('/Users/sapirchodorov/git_projects/crt/server.crt',
                   '/Users/sapirchodorov/git_projects/crt/server.key')  # certificate and key files
        app.run(host=self.server_ip, port=self.server_port,debug=True, ssl_context=context)


@app.route('/updateKey', methods=['POST'])
def update_server_key():
    req_body = request.json
    s.update_key(req_body['key_a'], req_body['key_d'])
    return Response(jsonify({"updated": True}), status=200, mimetype='application/json')


@app.route('/getKey', methods=['GET'])
def get_server_tag():
    y_tag = s.get_key_tag()
    return Response(jsonify(y_tag), status=200, mimetype='application/json')


@app.route('/testConnection', methods=['POST'])
def test_connection():
    req_body = request.json
    status = s.test_connection(req_body['clientKey'])
    if status:
        return Response(jsonify({"ConnectionAccepted": True}), status=200, mimetype='application/json')
    return Response(jsonify({"ConnectionAccepted": False}), status=405, mimetype='application/json')


if __name__ == '__main__':
    s = Server('127.0.0.1', 5000)
    s.serve()
