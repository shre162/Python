##mutlithreading
##when to use
##ans: I/O-bound tasks: tasks that spends more time waiting for I/O operations.(eg:file operation, network requests)
##concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers:{i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")

##create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()

##start the threads
t1.start()
t2.start()

##wait for the thread to  complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)

