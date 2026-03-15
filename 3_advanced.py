def transporent_decorstor(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def log_args_and_kwargs(func):
    def wrapper(*args, **kwargs):
        print(f"args: {args} | kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def forbid_kwargs(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("Keyword arguments are forbidden")
        return func(*args, **kwargs)

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def full_cycle_logger(func):
    def wrapper(*args, **kwargs):
        print("--- START ---")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        print("--- END ---")
        return result

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")
from functools import wraps


def perfect_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("--- Before ---")
        func()
        print("--- After ---")
        print(func.__name__)
        print(func.__doc__)

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


#######################################################################################################################
print(f"{'*'*100}")

import time


def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


#######################################################################################################################
print(f"{'*'*100}")


def outer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Outer Before")
        func(*args, **kwargs)
        print("Outer After")

    return wrapper


def inner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Inner Before")
        func(*args, **kwargs)
        print("Inner After")

    return wrapper


# Напишите декоратор @inner
# Ваш код здесь


@outer
@inner
def action():
    print("ACTION")


#######################################################################################################################
print(f"{'*'*100}")

#######################################################################################################################
print(f"{'*'*100}")
