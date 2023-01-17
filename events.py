import threading

# create event
event = threading.Event()

# this function waits for the vent to trigger
def myfunction():
    print("Waiting for the event to trigger...\n")
    # call wait function of the event, this makes our function wait until the event is triggered
    event.wait()
    print("Performing action xyz now......")

t1 = threading.Thread(target=myfunction)
# nothing happens until it is triggered
t1.start()

# user input
x = input("Do you want to trigger the event? (y/n) ")
if x == "y":
    # activate the event
    event.set()