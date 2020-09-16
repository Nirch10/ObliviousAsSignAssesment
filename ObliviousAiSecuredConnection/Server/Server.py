from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify
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

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    context = ('/Users/sapirchodorov/git_projects/crt/server.crt', '/Users/sapirchodorov/git_projects/crt/server.key')  # certificate and key files
    app.run(debug=True, ssl_context=context)
