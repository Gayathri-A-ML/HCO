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
        with open(f'{directory}/{path.name}') as f_obj:
            contents = str(f_obj.read())

        name = 'new_file' + str(i)
        i = i + 1
        # Open a new file to write the list of moves into.
        f = open(name, "w")
        f.write(contents)
        f.close()
    t2 = time.time()
    print(t2-t1)


asyncio.run(main())