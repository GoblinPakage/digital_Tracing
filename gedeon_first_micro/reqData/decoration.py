from functools import wraps
import time
import logging

def exectionTime_decoration(func):
    @wraps(func)
    def execution(*args, **kwargs):
        # calculate total execution time
        result=func(*args, **kwargs)
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        value = end_time - start_time

        # calculate the execution time
        # get the average execution time
        logging.debug(f'Function {func.__name__} Execution time is { value } seconds')
        print(f'Function {func.__name__} Execution time is { value } seconds')
        return result
    return execution

        