import abc
from random import randrange


class SignatureCreator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'sign') and
                callable(subclass.sign))


class ServerSignatureCreator:
    def __init__(self):
        self.p = 0;
        self.d = -1

    def set_p(self, p: int) -> None:
        self.p = p

    def sign(self, a: int, d: int) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : Y’ = Y + a % p.
        :rtype: int : y' result of the signature formula
        :param a: a param from sign generator which will be used in the formula
        :param d: d param from sign generator to compare the sender's signature with.
        """
        y = randrange(0, self.p);
        self.d = d
        y_tag = (y + a) % self.p
        return y_tag


class ClientSignatureCreator:
    def __init__(self):
        self.p = 0;

    def set_p(self, p: int) -> None:
        self.p = p

    def sign(self, b: int, c: int, y_tag: int) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : Z = (Y’ - X - b)*c % p.
        :param y_tag: the result of the server signature
        :rtype: int : z result of the signature formula
        :param b: b param from sign generator which will be used in the formula
        :param c: c param from sign generator to compare the sender's signature with.
        """
        x = randrange(0,100)
        z = ((y_tag - x - b) * c) % self.p
        return z


class ProxySignatureCreator:
    def __init__(self):
        self.p = 0
        # self.a = random(self.p)
        # self.b = random(self.p)
        # self.c = random(self.p)

    def sign(self, a: int, b: int, c: int, p: int) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : d = (a - b)*c % p.
        :rtype: int : z result of the signature formula
        """
        a = randrange(0, p)
        b = randrange(0, p)
        c = randrange(0, p)
        d = ((a - b) * c) % p
        return d
