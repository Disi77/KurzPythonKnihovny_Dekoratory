# Domácí úkol:
# 5) Napiš dekorátor, který zakáže printy. Pokude bude dekorovaná funkce něco vypisovat printem,
# tento výpis se neukáže, ale funkce bude dále normálně fungovat a vracet výsledky.


import my_decorator


@my_decorator.bez_printu
def funkce():
    print("Něco tisknu uvnitř funkce")
    return "A něco jiného vracím"


if __name__ == "__main__":
    print(funkce())
