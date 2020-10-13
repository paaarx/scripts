import yaml


def safe_read_yaml_file(yaml_file: str) -> dict:
    with open(yaml_file) as file:
        try:
            return yaml.safe_load(file)
        except FileNotFoundError as error:
            print(error)
        except yaml.YAMLError as error:
            print(error)
