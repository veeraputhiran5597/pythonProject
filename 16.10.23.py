import time
# from threading import Thread

from threading import *

# def a():
#     print("1")
# def b():
#     time.sleep(5)
#     print("2")
# def c():
#     print("3")
# a()
# b()
# c()

# def a():
#     print("1")
# def b():
#     time.sleep(5)
#     print("2")
#
# abc=Thread(target=a)
# abc.start()
# cba=Thread(target=b)
# cba.start()

def a():
    print(current_thread().getName())
def b():
    print(current_thread().getName())

abc=Thread(target=a)
abc.start()
cba=Thread(target=b)
cba.start()

# shedule-namakudukura time la function run akum
# thread-ore tome la multiple fun run akum-parlel aa run akum