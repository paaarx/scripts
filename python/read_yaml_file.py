import yaml


def read_yaml_file(yaml_file: str) -> dict:
    with open(yaml_file) as file:
        try:
            return yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError as error:
            print(error)
        except yaml.YAMLError as error:
            print(error)
