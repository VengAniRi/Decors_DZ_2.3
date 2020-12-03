from datetime import datetime as dt

# Декоратор с параметром
def path_logger_dec(fpath):
    def logger_dec(func):
        def wrapped(*args, **kwargs):
            moment = dt.today().strftime("%H:%M %d.%m.%Y")
            st = f"{moment} function {func.__name__} called\n"\
                 f"positional arguments: {args}\nkeyword arguments: {kwargs}\n" 
            result = func(*args, **kwargs)
            st += f"Returned value = {result}\n"
            with open(fpath, "a", encoding="utf-8") as f:
                f.write(st+"\n")
            return result
        return wrapped
    return logger_dec

# Демонстрация декоратора "log.txt"
@path_logger_dec("log.txt")
def my_func(x, y):
    x = x * y
    return x

@path_logger_dec("log.txt")
def foo(a, b=3, c=5):
    return a + b + c


my_func([0], 3)
foo(2, c=4)
