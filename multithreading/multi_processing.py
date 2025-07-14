##it allows you to create processes that run in parallel.
##when to use: CPU bound task(so tasks that are heavy on CPU usage ex.mathamatical computations or data processing)
##parallel execution-multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2.5)
        print(f"num:{i*i*i}")

if __name__=="__main__":
    
    ##create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()
    ##start the process
    p1.start()
    p2.start()

    ##wait for the process to complete
    p1.join()
    p2.join()
    finished_time= time.time()-t
    print(finished_time)
