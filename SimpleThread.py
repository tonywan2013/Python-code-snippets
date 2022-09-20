from time import sleep
from threading import Thread

class CustomThread(Thread):
    val = None
    def run(self):
        sleep(1)
        print("Set instance variable")
        self.val = 99
        print("Message from CustomThread")

thread = CustomThread()
thread.start()

print("Waiting for other thread to complete")
thread.join()

print("get result from other thread", thread.val)
print("Program completed")
