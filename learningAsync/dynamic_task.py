import asyncio


def say_intercept():
    print('intercept')


async def say_hello():
    await asyncio.sleep(1)
    print('world')


def main():
    print('hello')


loop = asyncio.get_event_loop()

loop.call_soon(main)
asyncio.ensure_future(say_hello())
loop.call_soon(say_intercept)

loop.run_forever()
loop.close()

