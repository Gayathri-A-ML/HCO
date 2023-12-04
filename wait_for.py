import asyncio

async def fun():
    print("A")
    await asyncio.sleep(2)
async def main():
    print("main function")
    await asyncio.create_task(asyncio.wait_for(fun(), 1))

asyncio.run(main())

#wait for function will wait for that particular time if that coroutine exceeded the time than it will give the timeout error