#######################################################################################################################
import time

print(f"{'*'*100}")


def precise_timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} sec.")
        return result

    return wrapper


def add_duration_to_dict(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        duration = end_time - start_time
        result["execution_time"] = duration
        return result

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def full_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned '{result}'")
        return result

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if cache.get(args):
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            return result

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")

import inspect


def validate_string_argument(**expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            print(bound_args)
            bound_args.apply_defaults()
            for name, value in bound_args.arguments.items():
                if name in expected_types and not isinstance(
                    value, expected_types[name]
                ):
                    raise TypeError("Argument must be a string")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_string_argument(text=str)
def process_text(text):
    print(f"Processing text: {text}")


process_text("123")


def validate_string_argument(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        if "text" in kwargs and not isinstance(kwargs["text"], str):
            raise TypeError("Argument must be a string")
        if args and not isinstance(args[0], str):
            raise TypeError("Argument must be a string")
        return func(*args, **kwargs)

    return wrapper


@validate_string_argument
def process_text(text):
    print(f"Processing text: {text}")


process_text(text="123")
process_text("123")


#######################################################################################################################
print(f"{'*'*100}")


def ensure_positive_number(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 0 or not isinstance(args[0], int):
            raise ValueError("Argument must be a positive number")
        return func(*args, **kwargs)

    return wrapper


def validate_user_role(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("role") != "admin":
            raise PermissionError("Access denied")
        return func(*args, **kwargs)

    return wrapper


def check_arg_count(func):
    def wrapper(*args, **kwargs):
        if len(args) != 2:
            raise ValueError("Function requires exactly 2 arguments")
        return func(*args, **kwargs)

    return wrapper


def no_empty_strings(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, str) and value == "":
                raise ValueError("Empty strings are not allowed")
        return func(*args, **kwargs)

    return wrapper


@no_empty_strings
def register_user(username, password):
    print(f"User '{username}' registered.")


register_user(username="", password=123)
