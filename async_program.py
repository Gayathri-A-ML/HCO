import asyncio


async def main():
    print("main function")
    #foo("text")  RuntimeWarning: coroutine 'foo' was never awaited  because async function need to call by using the event loop
    #await foo("text")  # in this function it will wait for 1 sec then its printing the finished  o/p main func inside foo finished
    task = asyncio.create_task(foo("text")) # If we don't want to wait for foo to complete  o/p main func finished inside foo
    #await task  #o/p main func inside foo finished after this task completes then remaining part of this func will work
    print("finished")
    await asyncio.sleep(1)  # o/p main fun inside foo at end foo finished
    print("at end")

async def foo(text):
    print("inside foo function")
    await asyncio.sleep(1)
    print("foo finished")


# main() //RuntimeWarning: coroutine 'main' was never awaited   because if we need to call the async function we should call with coroutine, if we make a call to function main() it return to coroutine
#await main() // await should be inside the async function
asyncio.run(main()) #asyncio internally create a event loop and in that loop coroutine main will be added and called