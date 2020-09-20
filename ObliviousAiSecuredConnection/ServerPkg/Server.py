import json

from flask import Flask, jsonify, request, Response

from Utils.HttpsConnector import HttpsServer
from Utils.abstractSign import ServerSignatureCreator


app = Flask(__name__)


def create_response(data, code: int, mimetype: str = 'application/json') -> app.response_class:
    """
    creates and returns a response for the server
    :param data: data to create json body for response
    :param code: http code
    :param mimetype: type of response (default json)
    :return: app.response_class type for the server to return to the client
    """
    response = app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype=mimetype
    )
    return response


class Server(HttpsServer, ServerSignatureCreator):

    def __init__(self, p_value: int, ip: str, port: int, certificate_path: str, certificate_key_path: str):
        super(Server, self).__init__(ip, port,certificate_path, certificate_key_path)
        ServerSignatureCreator.__init__(Server, p_value)
        self.y_tag = -1

    @staticmethod
    @app.route('/')
    def welcome() -> object:
        return Response(jsonify({"Welcome to my server": 'ss'}), status=200)

    def update_key(self, a: int, d: int) -> int:
        """
        calculates this server keys according to the formula
        :param a:
        :param d:
        :return: the public key generated
        """
        if self.y_tag == -1:
            self.y_tag = super(Server, self).sign(a, d)
            return self.y_tag
        else:
            return -1

    def get_public_key(self) -> int:
        return self.y_tag

    def test_connection(self, predicted_key) -> bool:
        """
        checks weather the predicted key equals to the server's secret key
        :param predicted_key:
        :return: true if they are equal, else false
        """
        if self.d == -1 or self.y_tag == -1:
            return False
        return predicted_key == self.d

    def serve(self):
        try:
            app.run(host=self.server_ip, port=self.server_port, debug=True, ssl_context=self.context)
        except:
            print("server {"+self.server_ip+"} not running on port: " + str(self.server_port))


@app.route('/updateKey', methods=['POST'])
def update_server_key():
    """
    update's the servers parameters for the formula and calculates it
    :return:
    """
    req_body = request.json
    server.update_key(req_body['key_a'], req_body['key_d'])
    response = create_response({"updated": True}, 200)
    return response


@app.route('/getKey', methods=['GET'])
def get_server_tag():
    """
    gets the server public result of the formula (server.y_tag)
    :return:
    """
    y_tag = server.get_public_key()
    response = create_response({'key': y_tag}, 200)
    return response


@app.route('/testConnection', methods=['POST'])
def test_connection():
    """
    tests if the request came from the same secret holder
    :return: response representing the answer of weather this is the chosen client
    """
    req_body = request.json
    status = server.test_connection(req_body['clientKey'])
    if status:
        response = create_response({"ConnectionAccepted": True, "Message": "You are the chosen one! we share the same "
                                                                           "secret :)"}, 200)
    else:
        response = create_response({"ConnectionAccepted": False, "Message": "Sorry, you are not the chosen one, "
                                                                            "my secrets will not be shared with "
                                                                            "you"}, 405)
    return response


def start_server(p_value: int, ip: str, port: int, certificate_path: str, certificate_key_path: str) -> None:
    """
    Start serving https server for algorithm check.
    :param p_value: the p value for the formula
    :param ip:
    :param port:
    :param certificate_path:
    :param certificate_key_path:
    """
    global server
    server = Server(p_value, ip, port, certificate_path, certificate_key_path)
    server.serve()
