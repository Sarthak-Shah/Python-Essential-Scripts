

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Call functions with arbitrary arguments
add(5, 10)
greet("Alice")
greet("Bob", greeting="Hi")
