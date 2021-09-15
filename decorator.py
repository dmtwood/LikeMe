
def my_decorator_args(nrofexecutions = 1):
    def wrapper_wrapper(func):
        def wrapper(*args, **kwargs):
        print("Before decorated function execution")
        for _ in range[nrofexecutions]:
            func(*args, **kwargs)
        print("After decorated function execution")
        return func(*args, **kwargs)
    return wrapper
    return wrapper_wrapper


@my_decorator(nrofexecutions)
def get_id( name, age=None):
    if age is not None:
        return name, age
    return name



