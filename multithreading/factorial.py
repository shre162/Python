import multiprocessing
import math
import multiprocessing.pool
import sys
import time

##increase the max num of digit for int conversion
sys.set_int_max_str_digits(100000)

##function to compute factorials of a given num
def computer_factorial(namber):
    print(f"computing factorial of {number}")
    result= math.factorial(number)
    print(f'factorial of {number} is {result}')
    return result
if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()
    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)
    
    end_time=time.time()
    print(f"results:{results}")
    print(f"time taken: {end_time-start_time}seconds")