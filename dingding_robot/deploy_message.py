import aiohttp
import asyncio
import json
from util import get_config

session = aiohttp.ClientSession()


def send_start_deploy_msg(project_name):
    send_message(
        get_config()['robotUrl'],
        json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}开始部署'
        }))


def send_finish_deploy_msg(project_name):
    send_message(
        get_config()['robotUrl'],
        json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}部署完毕'
        }))


def send_message(url, message):
    asyncio.ensure_future(session.post(url, data=message))
