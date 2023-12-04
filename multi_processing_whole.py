from multiprocessing import Process, Queue, current_process
import time
import queue #imported for using the queue.Empty exception



def do_the_job(task_queue_obj, completed_task_queue_obj):
    
    while True:
        try:
            '''
             try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            task = task_queue_obj.get_nowait()
        except queue.Empty:
            print("exception occured ")
            break;
        else:
            com_task = "task "+ str(task) +" is done by current process" + current_process().name
            completed_task_queue_obj.put(com_task)
            time.sleep(.5)
    return True

def main():

    number_of_task = 10
    number_of_process = 4
    task_queue_obj = Queue()
    completed_task_queue_obj = Queue()

    print("pushing all the task to task_queue ")
    for task in range(number_of_task):
        task_queue_obj.put(str(task))
    process = []
    print("task queue", task_queue_obj.get())
    for pro in range(number_of_process):
        proc = Process(target=do_the_job, args=(task_queue_obj, completed_task_queue_obj))
        process.append(proc)
        proc.start()
    for proc in process:
        proc.join()

    while not completed_task_queue_obj.empty():
        print(completed_task_queue_obj.get())


if __name__=='__main__':
    main()



"""
pushing all the task to task_queue 
task queue 0
exception occured 
exception occured 
exception occured 
exception occured 
task 1 is done by current processProcess-1
task 2 is done by current processProcess-2
task 3 is done by current processProcess-3
task 4 is done by current processProcess-4
task 5 is done by current processProcess-1
task 6 is done by current processProcess-2
task 7 is done by current processProcess-3
task 8 is done by current processProcess-4
task 9 is done by current processProcess-1
"""