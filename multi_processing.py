import multiprocessing as mp
import numpy as np
import time


def my_func(i, p1, p2, p3):
    res = p1 ** 2 * p2 + p3
    time.sleep(2)
    return (i, res)

def get_res(result):
    global res
    res.append(result)

    
if __name__ == '__main__':
    # params = np.random.random((10,3))*100
    # res = []
    # ts = time.time()
    # for i in range(0, 10):
    #     get_res(my_func(i, i+1, i+2, i+3))
    # print("time taken", time.time()- ts)
    # print(res)
    """
    time taken 20.015560388565063
[(0, 5), (1, 16), (2, 41), (3, 86), (4, 157), (5, 260), (6, 401), (7, 586), (8, 821), (9, 1112)]
    """
    params = np.random.random((10,3))*100
    cpu_count = mp.cpu_count()
    print("Available number of cpu " , cpu_count)
    pool = mp.Pool(cpu_count)
    res = []
    ts = time.time()
    for i in range(0, 10):
        pool.apply_async(my_func, args=(i, i+1, i+2, i+3), callback=get_res)

    pool.close()
    pool.join()
    print("time taken", time.time()- ts)
    print(res)

    """
    Available number of cpu  8
time taken 5.617616891860962
[(0, 5), (1, 16), (3, 86), (2, 41), (4, 157), (5, 260), (6, 401), (7, 586), (8, 821), (9, 1112)]
    """
