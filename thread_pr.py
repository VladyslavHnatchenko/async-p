from threading import Thread
import os, time, datetime, random, tracemalloc


tracemalloc.start()
children = 4
maxdelay = 6


def status():
    return ("Time: " + str(datetime.datetime.now().time()) +
            "\t Malloc, Peak: " + str(tracemalloc.get_traced_memory()))


def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess {num}, PID: {os.getpid()}, "
          f"Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")


if __name__ == "__main__":
    print(f"Parent PID: {os.getpid()}")
    for i in range(children):
        thr = Thread(target=child, args=(i,))
        thr.start()
