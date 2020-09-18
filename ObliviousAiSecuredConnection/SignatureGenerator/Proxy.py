import random
from abc import ABC

import self as self
from flask import Flask

from Server.AbstractServerClient import AbstractServer
from SignatureGenerator.abstractSign import ProxySignatureCreator


class SignatureGenerator(AbstractServer):
    @property
    def asset_dir(self):
        pass

    @property
    def app(self):
        return

    def __init__(self):
        self.signatureGen = ProxySignatureCreator()
        self.app = Flask(__name__)
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

        self.app.run(debug=True, ssl_context=context)


if __name__ == "__main__":
    SignatureGenerator().serve()
