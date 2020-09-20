from ClientPkg.Client import start_client
from Config import Config
from main import get_config_path

if __name__ == '__main__':
    config = Config(get_config_path())
    start_client(config.p_value, config.server_ip, config.server_port, config.generator_server_ip, config.generator_server_port
                 , config.certificate_path);