def flip(given_func):
    def wrapper(arg1, arg2):
        return given_func(arg2, arg1)
    return wrapper