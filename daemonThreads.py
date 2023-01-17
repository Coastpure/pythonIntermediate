# the scripts terminate even if the threads are running in the background

import threading
import time

# a daemon thread will be reading from a text file whereas the other thread will print it on the screen

path = "text.txt"
text = ""

# this function will run a constant loop that reads information from a file and waiting 3 seconds
# we are going to run this function in a daemon thread, so it's not important, even if it's an endless loop,
# we can terminate the loop without terminating it manually, but when the second thread(function) terminates it will also stop

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

# thirty times we are going to print what we have in the text
def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

# this thread is a daemon thread, so we are going to specify daemon=True
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

# it will print the text file, if you change the text as it runs, the output will also update and terminate after printing 30 times