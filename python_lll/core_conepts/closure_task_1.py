import time 
import functools 
import random 



def timer():
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                suck = func(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time 
                print(elapsed_time)
                return suck
            except Exception as e:
                raise(e)
        return wrapper
    return decorator



def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempts in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e: 
                    if attempts == max_attempts:
                        raise e 
        return wrapper
    return decorator



@timer()
@retry()
def call_function():
    ch = random.choice([True, False])
    if ch == True: 
        raise ConnectionError("Network Timeout")
    else: 
        return "Success!"



call_function()