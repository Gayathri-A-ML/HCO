import threading
import os
import time


def print_square(num):
    print("Square of num", num * num)
    time.sleep(2)
    print("ID of process running squaer program: {}".format(os.getpid()))
    print("Square thread name: {}".format(threading.current_thread().name))
 


def print_cube(num):
    print("Cube of num", num * num * num)
    time.sleep(2)
    print("ID of process running cube program: {}".format(os.getpid()))
    print("Cube thread name: {}".format(threading.current_thread().name))
 

if __name__=='__main__':
    print("Multi threading")
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")

"""

Multi threading
ID of process running main program: 30260
Main thread name: MainThread
Square of num 100
Cube of num 1000
ID of process running squaer program: 30260
Square thread name: Thread-1 (print_square)
ID of process running cube program: 30260
Cube thread name: Thread-2 (print_cube)
Done!

"""

