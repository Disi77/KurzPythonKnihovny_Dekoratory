# Domácí úkol:
# 1) Napiš dekorátor, který dekorovanou funkci doplní o výpis názvu funkce a argumentů — vhodné
# například pro ladění programu, abychom věděli, kdy a jak se funkce zavolá.
# 2) Napiš dekorátor, který změří čas, po který funkce pracuje a výsledek vypíše — také vhodné
# pro ladění, pokud nám přijde, že nějaká funkce trvá moc dlouho a chceme si to ověřit. Možno
# nakombinovat s prvním dekorátorem.


import my_decorator
import time
import random


@my_decorator.debug_message
def rectangle_area(a, b):
    """Function counts area of rectangle"""
    for i in range(random.randrange(50000000)):
        a == b
    return a*b


@my_decorator.debug_message
def yes_no(question):
    """Return true/false depending on whether the answer is yes/no"""
    while True:
        answer = input(question).lower().strip()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False


@my_decorator.debug_message
def bmi(*, height=182, weight=80):
    """BMI counter"""
    if height > 182:
        vystup = "You're taller than me"
    elif height == 182:
        vystup = "Your height is the same as mine"
    elif height < 182:
        vystup = "You're lower than me"
    return vystup + " and the weight is great too!"


@my_decorator.debug_message
def looking_for_keys():
    print(20*"►◄")
    print("Wait a minute until I find the keys....")
    sec = random.randrange(3, 10)
    for i in range(sec, 0, -1):
        print(f"{i} sec")
        time.sleep(1)
    print("Okay, we can go!")
    print(20*"►◄")


if __name__ == "__main__":
    a = 5
    b = 10
    print(f"I am counting area of reactangle where a = {a} and b = {b}...")
    print(f"and result is: {rectangle_area(a,b)}")
    print("\n\n")

    print(yes_no("Do you like coffee? y/n "))
    print("\n\n")

    print("BMI counter:")
    print(bmi(height=int(input("Your height: ")),
              weight=int(input("Your weight: "))))
    print("\n\n")

    looking_for_keys()
