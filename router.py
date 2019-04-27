from aiohttp import web
from handlers import docker_handlers
from dingding_robot import deploy_message


def get_route_config(routes):
    @routes.post('/{applicationName}')
    async def docker_compose_restart_handler(request):
        docker_handlers.docker_compose_restart(request.match_info['applicationName'])
        return web.Response(text="received, thank you")

    @routes.get('/{applicationName}')
    async def serve_test(request):
        return web.Response(text=f"app name {request.match_info['applicationName']}")

    @routes.post('/sendMessage')
    async def common_send_message(request):
        await print(request.json())
        # await deploy_message.send_message(request.json())
        return web.Response(text="message sent")
