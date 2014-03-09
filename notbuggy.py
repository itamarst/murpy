"""
Thread-safe variation.
"""

_counter = []

def increment():
    _counter.append(None)

def size():
    return len(_counter)
