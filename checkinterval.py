"""
Attempt to use sys.setcheckinterval() for testing.

So far not clear how to make failure deterministic.
"""

import sys, gc
sys.setcheckinterval(1)
import threading

import buggy
import notbuggy

def in_thread(start, end, f):
    start.set()
    for i in range(100):
        f()
    end.set()

def check_safety(f, assertion):
    def multiple():
        for i in range(100):
            f()
    start = threading.Event()
    end = threading.Event()
    threading.Thread(target=lambda: in_thread(start, end, f)).start()
    start.wait()
    multiple()
    end.wait()
    assert assertion()

check_safety(notbuggy.increment, lambda: notbuggy.size() == 200)
check_safety(buggy.increment, lambda: buggy.size() == 200)
