import asyncio

async def square_number(n):
    for i in range(1, n+1):
        print("Square of ", i, "is ", i**2)
        await asyncio.sleep(0.001)


async def main():

    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(square_number(3))
        task_group.create_task(square_number(4))

asyncio.run(main())

"""
Square of  1 is  1
Square of  1 is  1
Square of  2 is  4
Square of  2 is  4
Square of  3 is  9
Square of  3 is  9
Square of  4 is  16
both the task ran concurrently 
"""