# Domácí úkol:
# 5) Napiš dekorátor, který zakáže printy. Pokude bude dekorovaná funkce něco vypisovat printem,
# tento výpis se neukáže, ale funkce bude dále normálně fungovat a vracet výsledky.


import my_decorator


@my_decorator.without_print
def dummy_function():
    print("I print something inside the function")
    return "I return some value from the function"


if __name__ == "__main__":
    print(dummy_function())
