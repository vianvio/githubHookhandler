import asyncio


async def say_intercept():
    print('intercept')


async def say_hello():
    await asyncio.sleep(1)
    print('world')


async def main():
    print('hello')
    await say_hello()


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[asyncio.ensure_future(main()), asyncio.ensure_future(say_intercept())]))
loop.close()
