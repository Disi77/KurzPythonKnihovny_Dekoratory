# Domácí úkol:
# 4) Pokud ve funkci dojde k výjimce, dodá odkaz na google, který tu konkrétní chybu vyhledá.


import my_decorator
import random


@my_decorator.seach_python_error
def vyvolat_chybu():
    seznam = [ValueError, NameError, IndentationError, TypeError, SyntaxError]
    chyba = random.choice(seznam)
    print(f"Vyvolávám chybu: {chyba.__name__}")
    raise chyba


if __name__ == "__main__":
    vyvolat_chybu()
