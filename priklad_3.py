# Domácí úkol:
# 3) Napiš libovolný vlastní dekorátor.

import my_decorator
from random import randrange


@my_decorator.pocet_spusteni_funkce
def fizz_buzz(cislo):
    """Funkce vrací řetězec, pokud číslo odpovídá pravidlu,
       jinak vrací zadané číslo:
          *  FIZZ pokud je číslo dělitelné 3
          *  BUZZ pokud je číslo dělitelné 5
          *  FIZZ-BUZZ pokud je číslo dělitelné 3 i 5"""
    if cislo % 15 == 0:
        return "FIZZ-BUZZ"
    if cislo % 5 == 0:
        return "BUZZ"
    if cislo % 3 == 0:
        return "FIZZ"
    return cislo


@my_decorator.pocet_spusteni_funkce
def cisla_sportka():
    """Funkce vrátí seznam čísel pro Sportku"""
    cisla = []
    while len(cisla) < 6:
        cislo = randrange(1, 50)
        if cislo not in cisla:
            cisla.append(cislo)
    cisla.sort()
    return cisla


if __name__ == "__main__":
    for cislo in range(1, 151):
        print(fizz_buzz(cislo), end=' - ')

    print()
    sloupce = int(input("Losujeme čísla do Sportky, kolik sloupečků chceš vygenerovat? "))
    for s in range(1, sloupce+1):
        print(f"Čísla sloupec {s}: ", end="")
        print(cisla_sportka())
