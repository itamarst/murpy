"""
Some non-threadsafe code.
"""

_counter = 0

def increment():
    global _counter
    # Oops, not thread-safe if called multiple times:
    _counter = _counter + 1

def size():
    return _counter
