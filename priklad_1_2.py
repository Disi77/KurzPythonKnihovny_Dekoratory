# Domácí úkol:
# 1) Napiš dekorátor, který dekorovanou funkci doplní o výpis názvu funkce a argumentů — vhodné
# například pro ladění programu, abychom věděli, kdy a jak se funkce zavolá.
# 2) Napiš dekorátor, který změří čas, po který funkce pracuje a výsledek vypíše — také vhodné
# pro ladění, pokud nám přijde, že nějaká funkce trvá moc dlouho a chceme si to ověřit. Možno
# nakombinovat s prvním dekorátorem.


import my_decorator
import time
import random


@my_decorator.debug_vypis
def obsah_obdelniku(a, b):
    """Funkce vypočítá obsah obdelníku"""
    for i in range(random.randrange(100000, 200000)):
        a == b
    return a*b


@my_decorator.debug_vypis
def ano_ne(otazka):
    """Funkce vrací true nebo false podle toho, zda je odpověď ANO nebo NE"""
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved in ["a", "ano"]:
            return True
        elif odpoved in ["n", "ne"]:
            return False


@my_decorator.debug_vypis
def bmi(*, vyska=182, vaha=80):
    """Podle zadané výšky a váhy ti řekne, jak jsi na tom"""
    vystup = ''
    if vyska > 182:
        vystup += "Jsi vyšší než já"
    elif vyska == 182:
        vystup += "Tvá výška je stejná jako mám já"
    elif vyska < 182:
        vystup += "Jsi nižší než já"
    return vystup + " a váha je taky super!"


@my_decorator.debug_vypis
def hledam_klice():
    print(20*"►◄")
    print("Počkej chvilku, než najdu klíče ....")
    sec = random.randrange(3, 10)
    for i in range(sec, 0, -1):
        print(f"{i} vteřiny")
        time.sleep(1)
    print("Dobrý, mužeme jít!")
    print(20*"►◄")


if __name__ == "__main__":
    print(f"Počítám obsah obdelníku a výsledek je {obsah_obdelniku(5,10)}")
    print(ano_ne("Máš rád kávu? a/n "))
    print("BMI program: zadej svou výšku a váhu:")
    print(bmi(vyska=int(input("Zadej výšku: ")), vaha=int(input("Zadej váhu: "))))
    hledam_klice()
