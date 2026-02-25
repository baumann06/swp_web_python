import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        laufzeit = end - start
        print(f"Finished {func.__name__}() in {laufzeit:.4f} secs")
        return result
    return wrapper_timer