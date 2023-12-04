from multiprocessing import Pipe, Process

def send_msg(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("sent msg ", msg)
    conn.close()

def recive_msg(conn):
    while True:
        msg = conn.recv()
        if msg == 'END':
            break
        print("msg received ", msg)

def main():

    msgs = ['abc', 'start' , 'xyz', 'rrt', 'END']
    parent_con, child_con = Pipe()
    p1 = Process(target=send_msg, args=(parent_con, msgs))
    p2 = Process(target=recive_msg, args=(child_con,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=='__main__':
    main()



"""
sent msg  abc
sent msg  start
sent msg  xyz
sent msg  rrt
sent msg  END
msg received  abc
msg received  start
msg received  xyz
msg received  rrt
"""