import asyncio
import time

async def fun():
    print("async function")
    await asyncio.sleep(1)
    print(time.time())
    print("sleep1")
    await asyncio.sleep(1)
    print(time.time())
    print("sleep2")

asyncio.run(fun())