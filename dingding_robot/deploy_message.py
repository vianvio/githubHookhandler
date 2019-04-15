import aiohttp
import json
from util import get_config

_clientSession = aiohttp.ClientSession()


async def send_start_deploy_msg(project_name):
    await _clientSession.post(
        get_config()['robotUrl'],
        data=json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}开始部署'
        }))


async def send_finish_deploy_msg(project_name):
    await _clientSession.post(
        get_config()['robotUrl'],
        data=json.dumps({
            'msgtype': 'text',
            'text': f'{project_name}部署完毕'
        }))
