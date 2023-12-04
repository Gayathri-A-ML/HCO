import asyncio
import aiofiles
import time
from pathlib import Path

def read_file_with_normal_method(directory):
    pathlist = Path(directory).glob('*.txt')

    # Iterate through all json files in the directory.
    i = 0
    t1 = time.time()
    for path in pathlist:
        # Read the contents of the json file.
        with open(f'{directory}/{path.name}') as f_obj:
            contents = str(f_obj.read())

        name = 'new_file' + str(i)
        i = i + 1
        # Open a new file to write the list of moves into.
        f = open(name, "w")
        f.write(contents)
        f.close()
    t2 = time.time()
    return t2-t1

async def read_file_with_aiofiles(directory):
    pathlist = Path(directory).glob('*.txt')

    # Iterate through all json files in the directory.
    i = 0
    t1 = time.time()
    for path in pathlist:
        # Read the contents of the json file.
        async with aiofiles.open(f'{directory}/{path.name}', mode='r') as f:
            contents = await f.read()

        name = 'new_file' + str(i)
        i = i + 1
        # Open a new file to write the list of moves into.
        async with aiofiles.open(f'{directory}/{name}_moves.txt', mode='w') as f:
            await f.write('\n'.join(contents))
    t2 = time.time()
    return t2-t1
    


async def main():
    
    directory = 'D:\HCO\Program'
    print("Reading and writing the file by using aiofiles")
    time_taken = await read_file_with_aiofiles(directory)
    print('Time taken to read the file by using aiofiles', str(round(time_taken, 2)))

    print("Reading and writing the file by normal method")
    time_taken =  read_file_with_normal_method(directory)
    print('Time taken to read the file by normal method', str(round(time_taken, 2)))


asyncio.run(main())

