from dataclasses import dataclass
from functools import update_wrapper


@dataclass
class DecoratorClass:
    func: callable

    def __post_init__(self):
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        print("--- Before ---")
        result = self.func(*args, **kwargs)
        print("--- After ---")


class DecoratorClass:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        print("--- Before ---")
        result = self.func(*args, **kwargs)
        print("--- After ---")


#######################################################################################################################
print(f"{'*'*100}")


def instance_level_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args[0].counter += 1
        return func(*args, **kwargs)

    return wrapper


#######################################################################################################################
print(f"{'*'*100}")


#######################################################################################################################
print(f"{'*'*100}")


#######################################################################################################################
print(f"{'*'*100}")
