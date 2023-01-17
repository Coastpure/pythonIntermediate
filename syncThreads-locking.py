# LOCKING - limit access to a resource
import threading
import time

x = 8192

# this lock will forbid us or allow us to access the resource
lock = threading.Lock()

def double():
    # whenever I wanna access my resource, I have to lock it
    global x, lock
    # lock.acquire tries to acquire the lock if it's free
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # wait for 1 sec so that we can see what's happening
    print("Reached the maximum")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

# the first action to be executed will lock the resource until it finishes, then it will release the resource and the other function will start
# basically only one thread at a time can access the resource

