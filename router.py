from aiohttp import web
import asyncio
from handlers import docker_handlers
from dingding_robot import deploy_message
from aiojobs.aiohttp import spawn
import aiojobs

loop = asyncio.get_event_loop()

def get_route_config(routes):
    @routes.post('/sendMessage')
    async def common_send_message(request):
        deploy_message.send_message(await request.text())
        return web.Response(text="message sent")

    @routes.post('/{applicationName}')
    async def docker_compose_restart_handler(request):
        project_name = request.match_info['applicationName']
        await deploy_message.send_start_deploy_msg(project_name)
        await spawn(request, docker_handlers.handle_docker_restart(project_name))
        return web.Response(text="received, thank you")

    @routes.get('/{applicationName}')
    async def serve_test(request):
        return web.Response(text=f"app name {request.match_info['applicationName']}")
