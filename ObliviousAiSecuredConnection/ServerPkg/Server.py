import json

from flask import Flask, jsonify, request, Response
import os

from Utils.HttpsConnector import HttpsServer
from Utils.abstractSign import ServerSignatureCreator

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


def create_response(data, code: int, mimetype: str) -> app.response_class:
    response = app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype=mimetype
    )
    return response


class Server(HttpsServer, ServerSignatureCreator):

    def __init__(self, ip: str, port: int):
        super(Server, self).__init__(ip, port)
        ServerSignatureCreator.__init__(Server)
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
        app.run(host=self.server_ip, port=self.server_port, debug=True, ssl_context=self.context)


@app.route('/updateKey', methods=['POST'])
def update_server_key():
    req_body = request.json
    server.update_key(req_body['key_a'], req_body['key_d'])
    response = create_response({"updated": True}, 200, 'application/json')
    return response


@app.route('/getKey', methods=['GET'])
def get_server_tag():
    y_tag = server.get_key_tag()
    response = create_response({'key': y_tag}, 200, 'application/json')
    return response


@app.route('/testConnection', methods=['POST'])
def test_connection():
    req_body = request.json
    status = server.test_connection(req_body['clientKey'])
    if status:
        response = create_response({"ConnectionAccepted": True}, 200, 'application/json')
    else:
        response = create_response({"ConnectionAccepted": False}, 405, 'application/json')
    return response


def start_server():
    global server
    server = Server('127.0.0.1', 5000)
    server.serve()
