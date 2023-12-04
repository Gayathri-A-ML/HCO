from multiprocessing import Process
import multiprocessing as mp


def withdraw(balance, lock):
    for _ in range(100000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def deposit(balance, lock):
    for _ in range(100000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_ops():
    balance = mp.Value('i',100)
    lock = mp.Lock()
    p1 = mp.Process(target=withdraw, args=(balance,lock))
    p2 = mp.Process(target=deposit, args=(balance,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Final vlaue", balance.value)



if __name__=='__main__':
    for _ in range(10):
        perform_ops()


"""
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
Final vlaue 100
"""