from threading import Thread
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.1)
            

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(0.1)

t1 = hello()
t2 = hi()

t1.start()

t2.start()
