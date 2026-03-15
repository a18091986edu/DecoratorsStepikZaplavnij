def greeter_factory(greeting: str):
    def name_greeting(name: str):
        return f"{greeting}, {name}!"

    return name_greeting


greting_1 = greeter_factory("Hello")
greeting_2 = greeter_factory("Привет")

print(greting_1("Ivan"))
print(greeting_2("Ivan"))

#######################################################################################################################
print(f"{'*'*100}")


def multiplier_factory(factor):
    def multiplier_number(number):
        return number * factor

    return multiplier_number


mf1 = multiplier_factory(2)
mf2 = multiplier_factory(3)

print(mf1(5))
print(mf2(5))

#######################################################################################################################
print(f"{'*'*100}")


def counter_factory():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


cf1 = counter_factory()
cf2 = counter_factory()

print(cf1())
print(cf1())
print(cf1())
print(cf2())
print(cf2())
print(cf1())

#######################################################################################################################
print(f"{'*'*100}")


def storage_factory(initial_value):
    def getter():
        return initial_value

    def setter(new_value):
        nonlocal initial_value
        initial_value = new_value

    return (getter, setter)


sf1 = storage_factory(5)
sf2 = storage_factory(10)


print(sf1[0]())
print(sf2[0]())
sf1[1](15)
print(sf1[0]())
print(sf2[0]())


#######################################################################################################################
print(f"{'*'*100}")


def conditional_function_factory(condition):
    return lambda: print("Action A") if condition else print("Action B")


cf1 = conditional_function_factory(True)
cf2 = conditional_function_factory(False)
cf1()
cf2()
#######################################################################################################################
print(f"{'*'*100}")


def start_finish_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("Finish")

    return wrapper


def test_function():
    print("Function body")


test_function = start_finish_decorator(test_function)
test_function()


@start_finish_decorator
def test_function():
    print("Function body")


test_function()


#######################################################################################################################
print(f"{'*'*100}")


def separator_decarator(func):
    def wrapper():
        print(f'{"*"*10}')
        func()
        print(f'{"*"*10}')

    return wrapper


@separator_decarator
def hello():
    print("Hello, Decorators!")


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
