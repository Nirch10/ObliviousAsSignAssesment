import abc
from random import randrange

p = 11


class SignatureCreator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'sign') and
                callable(subclass.sign))

    @classmethod
    def set_p(cls):
        pass


class ServerSignatureCreator(SignatureCreator):
    def __init__(self):
        self.p = p;
        self.d = -1;

    def sign(self, a: int, d: int) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : Y’ = Y + a % p.
        :rtype: int : y' result of the signature formula
        :param a: a param from sign generator which will be used in the formula
        :param d: d param from sign generator to compare the sender's signature with.
        """
        y = randrange(0, self.p);
        self.d = y
        y_tag = (y + a) % self.p
        return y_tag


class ClientSignatureCreator(SignatureCreator):
    def __init__(self):
        self.p = p

    def sign(self, b: int, c: int, y_tag: int) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : Z = (Y’ - X - b)*c % p.
        :param y_tag: the result of the server signature
        :rtype: int : z result of the signature formula
        :param b: b param from sign generator which will be used in the formula
        :param c: c param from sign generator to compare the sender's signature with.
        """
        x = randrange(0, 100)
        z = ((y_tag - x - b) * c) % self.p
        return z


class ProxySignatureCreator(SignatureCreator):
    def __init__(self):
        self.p = p

    def sign(self) -> int:
        """
        Server's signature for the secured connection will be calculated by the formula : d = (a - b)*c % p.
        :rtype: int : z result of the signature formula
        """
        a = randrange(0, self.p)
        b = randrange(0, self.p)
        c = randrange(0, self.p)
        d = ((a - b) * c) % self.p
        return {'a': a, 'b': b, 'c': c, 'd': d}
