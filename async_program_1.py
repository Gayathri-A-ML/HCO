import asyncio


async def fetch_data():
    print("start fetch fun")
    await asyncio.sleep(2)
    print("done fetching")
    return {'data':1}

async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    print("task")
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_num())
    #o/p error
    value = await task1 #task1 is returning the value so we need to wait till execution comp
    print(value) 
    #o/p start fetch fun 0 1 2 3 4 5 6 7 done fetching {'data':1} // its missing 8 and 9 because if task1 completes it finished if we need to complete task2 need to await task2
    await task2
     #o/p start fetch fun 0 1 2 3 4 5 6 7 done fetching 8 {'data':1} 9

asyncio.run(main())