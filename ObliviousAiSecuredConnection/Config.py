import json


class Config(object):
    def __init__(self, json_config_path: str):
        with open(json_config_path) as file:
            json_obj = json.load(file)
        self.server_ip = None if 'Ip' not in json_obj['ServerConfig'] else json_obj['ServerConfig']['Ip']
        self.server_port = None if 'Port' not in json_obj['ServerConfig'] else json_obj['ServerConfig']['Port']
        self.generator_server_ip = None if 'ServingIp' not in json_obj['KeyGeneratorConfig']\
            else json_obj['KeyGeneratorConfig']['ServingIp']
        self.generator_server_port = None if 'ServingPort' not in json_obj['KeyGeneratorConfig'] \
            else json_obj['KeyGeneratorConfig']['ServingPort']
        self.certificate_path = None if 'CertificatePath' not in json_obj['GlobalConfig'] \
            else json_obj['GlobalConfig']['CertificatePath']
        self.serve_certificate_path = None if 'ServerCertificatePath' not in json_obj['GlobalConfig'] \
            else json_obj['GlobalConfig']['ServerCertificatePath']
        self.serve_certificate_key_path = None if 'ServerCertificateKeyPath' not in json_obj['GlobalConfig'] \
            else json_obj['GlobalConfig']['ServerCertificateKeyPath']
        self.p_value = None if 'pValue' not in json_obj['GlobalConfig'] else json_obj['GlobalConfig']['pValue']


