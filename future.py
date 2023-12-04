
import asyncio
from asyncio import Future
#A future is an object that returns a value in the future, not now.
async def main():
    my_future = Future()
    print(my_future.done())  # False

    my_future.set_result('Bright')

    print(my_future.done())  # True

    print(my_future.result())


asyncio.run(main())