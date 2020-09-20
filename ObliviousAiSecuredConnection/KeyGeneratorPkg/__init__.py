from Config import Config
from KeyGeneratorPkg.KeyGenerator import start_generator
from main import get_config_path

if __name__ == '__main__':
    config = Config(get_config_path())
    start_generator(config.p_value, config.server_ip, config.server_port, config.generator_server_ip
                    , config.generator_server_port, config.certificate_path, config.serve_certificate_path
                    , config.serve_certificate_key_path)
