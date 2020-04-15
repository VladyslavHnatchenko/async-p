import asyncio


async def my_coro(delay):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + delay
    while True:
        print("Blocking...")
        await asyncio.sleep(1)
        if loop.time() > end_time:
            print("Done.")
            break


async def main():
    await my_coro(3.0)


asyncio.run(main())

# Simple EXAMPLE
# async def my_coro(arg):
#     arg = "A coroutine."
#     print(arg)
#
#
# async def main():
#     arg = "The top level coroutine."
#     await my_coro(42)
#
#
# asyncio.run(main())
