import yaml

CONFIG_PATH = "./configs/config.yaml"


def __main__():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)
    print(config["key"])
