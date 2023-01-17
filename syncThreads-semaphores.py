# SEMAPHORES - another useful way to limit access to a resource
# limit the access to a resource through a max value

import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access".format(thread_number))
    # to acquire the semaphore
    semaphore.acquire()
    print("{} was granted".format(thread_number))
    time.sleep(10)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

# create 10 threads that will all execute this function with a different thread number

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)


# args=(thread_number, how we pass in a parameter to that function
