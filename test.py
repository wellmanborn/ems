import asyncio
import time


def read_from_plc():
    time.sleep(2)
    return "read from plc"


async def write_to_db(data):
    print("write to db from " + data)
    for i in range(10000):

    await asyncio.sleep(5)



async def do_something():
    data = read_from_plc()
    asyncio.create_task(write_to_db(data))


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(do_something())
    asyncio.run(do_something())
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start)} second(s)')