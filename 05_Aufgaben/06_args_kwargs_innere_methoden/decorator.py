import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Funktionsname: "+func.__name__)
        print(f"Argumente: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"[REPEAT] Durchlauf {i+1}")
                count = 0
                for a in args:
                    count += 1
                for b in kwargs:
                    count += 1
                print(f"[REPEAT] Parameter: {count}")
                func(*args, **kwargs)
        return wrapper
    return decorator

