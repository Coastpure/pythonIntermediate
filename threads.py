# threading allows us to speed up our program by executing multiple tasks at the same time

import threading

def helloworld():
    print("Hello world")

# we need to create a new object of the thread class, so we say threading.Thread()
# here we don't call helloworld function by adding ()

h1 = threading.Thread(target=helloworld)
# to run/start the thread we can use the start() method
# h1.start()

# basically it just runs the function that we define
# the benefit of this is that we can execute 2 functions simultaneously.

def function1():
    for x in range(10000):
        print("ONE")

def function2():
    for x in range(10000):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

# t1.start()
# t2.start()


def hello():
    for x in range(50):
        print("Hello")

he = threading.Thread(target=hello)
he.start()

# if I don't want anything to happen until hello() finishes executing, we use .join()
he.join()

# this will wait for hello to finish then it will be executed
print("Another text")