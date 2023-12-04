import asyncio
import aiofiles
import time


def read_file_with_normal_method(filename):
    t1 = time.time()
    with open(filename) as f_obj:
            contents = str(f_obj.read())
    t2 = time.time()
    print(contents)
    return t2-t1


async def read_file_with_aiofiles(filename):
    t1 = time.time()
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
    t2 = time.time()
    print(contents)
    return t2-t1
    


async def main():
    
    filename ="D:\HCO\Program\snappy.txt"
    print("Reading the file by using aiofiles")
    time_taken = await read_file_with_aiofiles(filename)
    print('Time taken to read the file by using aiofiles', str(round(time_taken, 2)))

    print("Reading the file by normal method")
    time_taken =  read_file_with_normal_method(filename)
    print('Time taken to read the file by normal method', str(round(time_taken, 2)))


asyncio.run(main())

