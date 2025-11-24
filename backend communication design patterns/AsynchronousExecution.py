import asyncio
import aiofiles
import time
from pathlib import Path


async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
    print(f"{filename.name} has {len(content)} characters")
    await asyncio.sleep(1)
    print(content, end="\n\n")
    return content


async def main():
    base_dir = Path("data")
    files = [base_dir / f"file{i}.txt" for i in range(1, 4)]

    start = time.time()

    await asyncio.gather(*(read_file_async(file) for file in files))
    # generator expression, just like a loop produces one coroutine per file.
    # asterisk before it is the unpacking operator - it unpacks that generator objects into individual artumnets
    # more readable way
    # tasks = [read_file_async(file) for file in files]
    # results = await asyncio.gather(*tasks)

    end = time.time()
    print(f"Total time (async, aiofiles): {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
