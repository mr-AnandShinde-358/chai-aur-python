""" def debug(func):
    def wrapper():
        return func()
    return wrapper

def hellow():
    print("hellow")
   """  

""" def debug(func):
    # print(func)
    def wrapper(*args,**kwargs):
        # print(func())
        return func(*args,**kwargs)
    
    result = wrapper()
    return result
    # print(wrapper)
    # return wrapper

def hellow():
    print("hellow")

a = debug(hellow)
# a()
 """

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k,v in kwargs)
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args,**kwargs)
    return wrapper

@debug
def hellow():
    print("hellow")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting},{name}")

greet("chai","hanji")
hellow()