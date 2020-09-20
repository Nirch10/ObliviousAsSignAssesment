import abc
from random import randrange


class SignatureCreator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'sign') and
                callable(subclass.sign))

    @classmethod
    def set_p(cls, p):
        cls.p = p


class ServerSignatureCreator(SignatureCreator):
    def __init__(self, p: int):
        super().set_p(p)
        self.d = -1
        self.y = randrange(0, self.p)

    def sign(self, a: int, d: int) -> int:
        """
        ServerPkg's signature for the secured connection will be calculated by the formula : Y’ = Y + a % p.
        in the formula y is represented as a random number between 0 and self.p -1
        :rtype: int : y' result of the signature formula
        :param a: a param from sign generator which will be used in the formula
        :param d: d param from sign generator to compare the sender's signature with.
        """
        self.d = d
        y_tag = self.y + a % self.p
        return y_tag


class ClientSignatureCreator(SignatureCreator):
    def __init__(self, p: int):
        super().set_p(p);
        self.x = randrange(0, 100)

    def sign(self, b: int, c: int, y_tag: int) -> int:
        """
        ServerPkg's signature for the secured connection will be calculated by the formula : Z = (Y’ - X - b)*c % p.
        in the formula x is represented as a random int between 0 and self.p -1  (where self.p should be prime)
        :param y_tag: the result of the server signature
        :rtype: int : z result of the signature formula
        :param b: b param from sign generator which will be used in the formula
        :param c: c param from sign generator to compare the sender's signature with.
        """
        z = ((y_tag - self.x - b) * c) % self.p
        return z


class ProxySignatureCreator(SignatureCreator):
    def __init__(self, p: int):
        super().set_p(p);

    def sign(self) -> int:
        """
        ServerPkg's signature for the secured connection will be calculated by the formula : d = (a - b)*c % p.
        :rtype: int : z result of the signature formula
        """
        a = randrange(1, self.p)
        b = randrange(1, self.p)
        c = randrange(1, self.p)
        d = ((a - b) * c) % self.p
        return {'a': a, 'b': b, 'c': c, 'd': d}
