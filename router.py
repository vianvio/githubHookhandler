from aiohttp import web
import json


def get_route_config(routes):
    @routes.post('/{applicationName}')
    async def hello(request):
        print(json.dump(request))
        return web.Response(text="received, thank you")
