import json


def get_config():
    with open('./config.json', 'r', encoding='utf-8') as config_file:
        json.load(config_file.read())
