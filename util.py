import json


def get_config():
    with open('./config.json', 'r', encoding='utf-8') as config_file:
        return json.load(config_file)
