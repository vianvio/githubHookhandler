from aiohttp import web
from .handlers import docker_handlers


def get_route_config(routes):
    @routes.post('/{applicationName}')
    async def docker_compose_restart_handler(request):
        docker_handlers.docker_compose_restart(request.match_info['applicationName'])
        return web.Response(text="received, thank you")
