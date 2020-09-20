import os

from Config import Config


def get_config_path() -> str:
    return os.path.realpath('../Config.json')


if __name__ == '__main__':
    config = Config(get_config_path())
