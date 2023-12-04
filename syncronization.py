from multiprocessing import Process
import multiprocessing as mp


def withdraw(balance):
    for _ in range(100000):
        balance.value = balance.value - 1

def deposit(balance):
    for _ in range(100000):
        balance.value = balance.value + 1


def perform_ops():
    balance = mp.Value('i',100)
    p1 = mp.Process(target=withdraw, args=(balance,))
    p2 = mp.Process(target=deposit, args=(balance,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Final vlaue", balance.value)



if __name__=='__main__':
    for _ in range(10):
        perform_ops()


"""
Final vlaue 1120
Final vlaue 6342
Final vlaue -5831
Final vlaue -1656
Final vlaue -548
Final vlaue -1875
Final vlaue 506
Final vlaue -12448
Final vlaue -8472
Final vlaue -295


because at a time the shared resources were used to overcone this we can use the lock mechanisim refer lock.py
"""