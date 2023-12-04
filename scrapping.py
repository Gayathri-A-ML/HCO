from selenium import webdriver 
import asyncio
import time


async def scrape(url): 
    print("inside the function")
    driver = webdriver.Chrome() 
    driver.get(url) 
    page_source = driver.page_source 
    #print(page_source)
    driver.close()


async def sub_fun(urls):
    for url in urls:
        print("Started printing the url", url)
        await scrape(url)
        await asyncio.sleep(1)
    


async def main():
    print("Main function")
    total_time = 0
    start_time = time.time()
    urls1 = ['https://testdriven.io/blog/python-concurrency-parallelism/','https://www.geeksforgeeks.org/asyncio-in-python/']
    task1 = asyncio.create_task(sub_fun(urls1))
    await task1
    urls2 = ['https://www.geeksforgeeks.org/calendar-in-python/?ref=lbp','https://www.geeksforgeeks.org/python-collections-module/?ref=lbp']
    task2 = asyncio.create_task(sub_fun(urls2))
    await task2
    end_time = time.time()
    print("Time taken ", end_time - start_time)
    total_time += end_time - start_time
    print("Total time ", total_time)

asyncio.run(main())

