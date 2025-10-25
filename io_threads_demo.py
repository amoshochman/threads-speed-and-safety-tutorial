import threading
import time

import requests

TASKS_NUM = 100


class SomeClass:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def task_function(self, run_safe=True, call_url=True):
        if call_url:
            requests.get('http://localhost:8000')
        if run_safe:
            self.lock.acquire()
        prev_val = self.counter
        time.sleep(0.0001)
        self.counter = prev_val + 1
        if run_safe:
            self.lock.release()


def run_sequential():
    obj = SomeClass()
    for i in range(TASKS_NUM):
        obj.task_function()


def run_parallel(run_safe=True, call_url=True):
    obj = SomeClass()
    threads = []
    for i in range(TASKS_NUM):
        threads.append(threading.Thread(target=obj.task_function, args=(run_safe, call_url)))
    for i in range(TASKS_NUM):
        threads[i].start()
    for i in range(TASKS_NUM):
        threads[i].join()
    return obj.counter


def validate(counter):
    if counter == TASKS_NUM:
        print('all good, counter == TASKS_NUM')
    else:
        print('counter=' + str(counter) + ' != ' + 'TASKS_NUM=' + str(TASKS_NUM))


def show_data_safety():
    print('running the not safe version... ', end='')
    validate(run_parallel(run_safe=False, call_url=False))
    print('running the safe version... ', end='')
    validate(run_parallel(run_safe=True, call_url=False))


def show_concurrency_speed():
    start = time.time()
    run_sequential()
    print('time passed for sequential:' + str(time.time() - start))
    start = time.time()
    run_parallel()
    print('time passed for parallel:' + str(round(time.time() - start, 2)))


if __name__ == "__main__":
    show_data_safety()
    show_concurrency_speed()
