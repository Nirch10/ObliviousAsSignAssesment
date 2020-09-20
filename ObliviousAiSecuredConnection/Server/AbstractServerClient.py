import abc
import os
from abc import ABC, abstractclassmethod, ABCMeta, abstractproperty

from flask import Flask, jsonify


class AbstractServer(ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        # self.app = None
        self.server_ip = ''
        self.server_port = 'None'

    # @property
    # def app(self):
    #     return self._server_address
    #
    # @app.setter
    # def app(self, val):
    #     self._app = val

    @property
    def server_ip(self):
        return self._server_ip

    @server_ip.setter
    def server_ip(self, ip: str):
        self._server_ip = ip

    @property
    def server_port(self):
        return self._server_port

    @server_port.setter
    def server_port(self, port: int):
        self._server_port = port

    @abc.abstractmethod
    def serve(self):
        pass

class AbstractClient(ABC):
    pass
