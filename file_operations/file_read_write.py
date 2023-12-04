import aiofiles
import asyncio
import json
from pathlib import Path
import time



directory = 'D:\HCO\Program'


async def main():
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
    print(t2-t1)


asyncio.run(main())