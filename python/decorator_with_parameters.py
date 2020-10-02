import datetime
import time


def summary(start_time, end_time):
    time_elapsed = end_time - start_time
    print(f'Start Time: {start_time}')
    print(f'End Time: {end_time}')
    print(f'Elapsed Time: {time_elapsed}')


def timeit(enable=False):
    def decorator(original_method):
        def wrapper(*args, **kwargs):
            if enable:
                start_time = datetime.datetime.now()
                wrapped_method = original_method(*args, **kwargs)
                end_time = datetime.datetime.now()
                summary(start_time, end_time)
                return wrapped_method
            return original_method(*args, **kwargs)
        return wrapper
    return decorator


@timeit(enable=True)
def main():
    time.sleep(0.3)


if __name__ == "__main__":
    main()
