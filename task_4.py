# Domácí úkol:
# 4) Pokud ve funkci dojde k výjimce, dodá odkaz na google, který tu konkrétní chybu vyhledá.


import my_decorator
import random


@my_decorator.seach_python_error
def raise_exception():
    exception_list = [ValueError,
                      NameError,
                      IndentationError,
                      TypeError,
                      SyntaxError]
    exception_object = random.choice(exception_list)
    print(f"Exception name: {exception_object.__name__}")
    raise exception_object


if __name__ == "__main__":
    raise_exception()
