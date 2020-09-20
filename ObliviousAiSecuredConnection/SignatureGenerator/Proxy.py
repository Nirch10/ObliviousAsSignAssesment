import random
from typing import List

# import self as self

from Server.AbstractServerClient import AbstractServer
from SignatureGenerator.abstractSign import ProxySignatureCreator
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def get_client_numbers() -> List:
    return 'a'

class SignatureGenerator(AbstractServer):
    # @property
    # def app(self):
    #     return self._app

    def __init__(self, ip: str, port: int):
        super().__init__()
        self._server_ip = ip
        self._server_port = port
        self.signatureGen = ProxySignatureCreator()
        self.max_prime = 50
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.p = None

    def get_key(self):
        def randomize_values():
            primes = [i for i in range(0, self.max_prime) if random.isPrime(i)]
            self.p = random.choice(primes)
            self.a = random(self.p)
            self.c = random(self.p)
            self.b = random(self.p)

        if None in (self.a, self.b, self.c):
            randomize_values()
        self.d = self.signatureGen.sign()

    def serve(self):
        context = ('/Users/sapirchodorov/git_projects/crt/server.crt',
                   '/Users/sapirchodorov/git_projects/crt/server.key')  # certificate and key files
        app.run(host=self._server_ip, port=self._server_port, debug=True, ssl_context=context)
        self.get_key()




if __name__ == "__main__":
    SignatureGenerator('localhost', 5445).serve()
