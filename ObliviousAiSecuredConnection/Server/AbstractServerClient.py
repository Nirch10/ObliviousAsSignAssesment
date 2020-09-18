import os
from abc import ABC, abstractclassmethod, ABCMeta, abstractproperty

import flask as Flask


class AbstractServer(ABC):
    __metaclass__ = ABCMeta
    @property
    @abstractclassmethod
    def asset_dir(cls):
        os.path.dirname(os.path.abspath(__file__))

    def get_app(self):
        return self.app

    def set_app(self, val):
        pass

    @abstractclassmethod
    def serve(cls):
        pass;
    app = abstractproperty(get_app, set_app)

class AbstractClient(ABC):
    pass
