import time
import threading

def calc():
    a = 1

    for i in range(1,100001):
        a*=i
    

def calcHalf1():
    a = 1
    for i in range(1,33333):
        a*=i


def calcHalf2():
    a = 1

    for i in range(33333,66666):
        a*=i

def calcHalf3():
    a = 1

    for i in range(66666,100001):
        a*=i



start = time.time()

calc()

end = time.time() - start

startThread = time.time()

t1 = threading.Thread(target=calcHalf1)
t2 = threading.Thread(target=calcHalf2)
t3 = threading.Thread(target=calcHalf3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

endThread = time.time() - startThread

print("normal Time :",end)
print("Thread Time :",endThread)
