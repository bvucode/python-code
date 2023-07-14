def decoration(func):
    def wrapper():
        func()
        print("decoration")
    return wrapper

@decoration
def some_func():
    print("some_func")

some_func()
