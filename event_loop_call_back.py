
import asyncio

def callback(res):
    print("result ", res.result())

async def log_running_fun():
    print("log_running_fun")
    await asyncio.sleep(10)
    return 1 + 1

async def main():
    event_loop.create_task(log_running_fun()).add_done_callback(callback)
    print("main completed")

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.run_forever()

'''
In this program if we call the log_running_fun withour add_done_callback the result of func 1 +1 will not handle anywhere so we can add once that task coplete
that result should print at callback()
callback is used when out function completes execution and have the results
'''