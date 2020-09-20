from Config import Config


def get_config_path() -> str:
    return '/Users/sapirchodorov/git_projects/ObliviousAsSignAssesment/ObliviousAiSecuredConnection/Config.json';


if __name__ == '__main__':
    config = Config(get_config_path())
