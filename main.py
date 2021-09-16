import logging
from aiohttp import web
import asyncio
from router import get_route_config
import aiojobs


async def main():
    logging.basicConfig(level=logging.DEBUG, filename='/root/git-handler-log/deploy.log', format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    routes = web.RouteTableDef()

    get_route_config(routes)

    app = web.Application()
    app.add_routes(routes)
    # 任务队列
    aiojobs.aiohttp.setup(app)
    aiojobs.Scheduler.pending_limit = 2
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5000)
    await site.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
