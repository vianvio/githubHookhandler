import aiohttp
import asyncio
import json
from util import get_config

session = aiohttp.ClientSession()


async def send_start_deploy_msg(project_name):
    await send_message(f'一号汇报：\n{project_name}开始部署')


async def send_finish_deploy_msg(project_name):
    await send_message(f'一号汇报：\n{project_name}部署完毕')


async def send_message(message):
    headers = {'content-type': 'application/json'}
    await session.post(get_config()['robotUrl'], data=json.dumps({
        'msgtype': 'text',
        'text': {
            'content': message
        }
    }), headers=headers)
