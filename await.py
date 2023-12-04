import asyncio


async def main():
    print('main')
    task = asyncio.create_task(foo('txt'))
    await task
    print('abc')
    await asyncio.sleep(1)
    print('main finished')

async def foo(txt):
    print(txt)
    await asyncio.sleep(1)

asyncio.run(main())