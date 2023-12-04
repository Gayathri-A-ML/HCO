from multiprocessing import Process

def print_names(name):
    print(name)

def names_printing(name):
    print(name)
    
if __name__ == '__main__':
    names = ["Asia, Africa, Australia"]
    procs =[]
    for name in names:
        proc = Process(target=print_names, args=(name,))
        procs.append(proc)
        proc.start()
        proc = Process(target=names_printing, args=(name,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        print(proc)
        proc.join()
"""
<Process name='Process-1' pid=32276 parent=27076 started>
Asia, Africa, Australia
<Process name='Process-2' pid=1716 parent=27076 started>
Asia, Africa, Australia
"""