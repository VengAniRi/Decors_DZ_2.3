from datetime import datetime as dt

fname = "log.txt"

# Декоратор
def logger_dec(func):
    def wrapped(*args, **kwargs):
        moment = dt.today().strftime("%H:%M %d.%m.%Y")
        st = f"{moment} function {func.__name__} called\n"\
             f"positional arguments: {args}\nkeyword arguments: {kwargs}\n" 
        result = func(*args, **kwargs)
        st += f"Returned value = {result}\n"
        with open(fname, "a", encoding="utf-8") as f:
            f.write(st+"\n")
        return result
    return wrapped

# Демонстрация декоратора
@logger_dec
def my_func(x, y):
    x = x * y
    return x

@logger_dec
def foo(a, b=3):
    return a + b


my_func([0], 3)
foo(2)
