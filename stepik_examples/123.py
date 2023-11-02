import functools


def recviz(func):
    def visualize_function(func_name, func_args, level):
        indent = "    " * level
        print(f"{indent} -> {func_name}({func_args})")

    def visualize_return(return_value, level):
        indent = "    " * level
        print(f"{indent} <- {return_value}")

    def execute_recursively(level, *args, **kwargs):
        func_name = func.__name__
        func_args = ", ".join(map(repr, args))
        visualize_function(func_name, func_args, level)
        result = func(*args, **kwargs)
        visualize_return(result, level)
        return result
    

    @functools.wraps(func)
    def decorated_function(*args, **kwargs):
        level = -1
        def decorate(level=level, *args, **kwargs):
            level += 1
            return execute_recursively(level, *args, **kwargs)
        level -= 1
        return decorate(level, *args, **kwargs)
    return decorated_function

# Usage example:
@recviz
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the decorated function
result = factorial(4)

