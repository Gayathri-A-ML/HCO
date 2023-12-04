import asyncio

@asyncio.coroutine
def fun():
    print("fun")
    yield from asyncio.sleep(1)

async def main():
    await fun()