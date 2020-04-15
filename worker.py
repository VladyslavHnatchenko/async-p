# ThreadPoolExecutor VERSION
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, "hello")
print(future.done())
sleep(5)
print(future.done())
print(future.result())

# Multiprocessing VERSION
# import multiprocessing
# import time
# import random
#
#
# def worker(number):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print(f"I am Worker {number}, I slept for {sleep} seconds")
#
#
# for i in range(5):
#     t = multiprocessing.Process(target=worker, args=(i,))
#     t.start()
#
# print("All Processes are queued, let's see when they finish!")


# Threading VERSION
# import threading
# import time
# import random
#
#
# def worker(number):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print(f"I am Worker {number}, I slept for {sleep} seconds")
#
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#
# print("All Threads are queued, let's see when they finish!")
