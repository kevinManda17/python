#coding: utf-8

import time 
import threading

my_lock= threading.RLock()

class Myprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        i =0 
        while i <3 :
            # print(threading.current_thread())
            with my_lock:
                letters ="ABC"
                for lt in letters :
                    print(lt,threading.current_thread())
                time.sleep(0.6 )
                i += 1

# def process_one():
#     i =0 
#     while i <3 :
#         print("Kevin ")
#         time.sleep(0.7)
#         i += 1

# def process_two():
#     i=0 
#     while i<3 :
#         print("Manda ")
#         time.sleep(0.5)
#         i  += 1

thread1=Myprocess()
thread2=Myprocess()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("fin du programme ...")