import aiohttp
import asyncio
import json
from util import get_config

session = aiohttp.ClientSession()


def send_start_deploy_msg(project_name):
    send_message(
        json.dumps({
            'msgtype': 'text',
            'text': {
                'content': f'{project_name}开始部署'
            }
        }))


def send_finish_deploy_msg(project_name):
    send_message(
        json.dumps({
            'msgtype': 'text',
            'text': {
                'content': f'{project_name}部署完毕'
            }
        }))


def send_message(message):
    headers = {'content-type': 'application/json'}
    asyncio.ensure_future(session.post(get_config()['robotUrl'], data=message, headers=headers))
