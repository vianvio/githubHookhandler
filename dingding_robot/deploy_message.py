import requests
import json
from util import get_config


def send_start_deploy_msg(project_name):
    requests.post(
        get_config()['robotUrl'],
        data=json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}开始部署'
        }))


def send_finish_deploy_msg(project_name):
    requests.post(
        get_config()['robotUrl'],
        data=json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}部署完毕'
        }))
