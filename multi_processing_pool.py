from multiprocessing import Pool
import time

work = (['A',1],['B', 3],['c',2],['D',5])

def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])

def main():
    p = Pool(3)
    p.map(work_log, work)
if __name__=='__main__':
    main()


"""
Process A waiting 1 seconds
 Process B waiting 3 seconds
 Process c waiting 2 seconds
 Process A Finished.
 Process D waiting 5 seconds
 Process c Finished.
 Process B Finished.
 Process D Finished.

 If the number of pool is increased time will decrease
"""