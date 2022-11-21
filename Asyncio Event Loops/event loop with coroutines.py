import asyncio


async def myCoroutine():
    while True:
        await asyncio.sleep(2)
        print("My first coroutine !")


async def secondCoroutine():
    while True:
        await asyncio.sleep(1)
        print("My second coroutine !")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(myCoroutine())
    asyncio.ensure_future(secondCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop !")
    loop.close()

