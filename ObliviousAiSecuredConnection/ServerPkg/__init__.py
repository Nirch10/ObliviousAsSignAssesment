from Config import Config
from ServerPkg.Server import start_server
from main import get_config_path

if __name__ == '__main__':
    config = Config(get_config_path())
    start_server(config.p_value, config.server_ip, config.server_port, config.serve_certificate_path, config.serve_certificate_key_path)
