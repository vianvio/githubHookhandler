from aiohttp import web
from .router import get_route_config

def main():
    routes = web.RouteTableDef()

    get_route_config(routes)

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
