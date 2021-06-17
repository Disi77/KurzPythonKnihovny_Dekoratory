# Domácí úkol:
# 1) Napiš dekorátor, který dekorovanou funkci doplní o výpis názvu funkce a argumentů — vhodné
# například pro ladění programu, abychom věděli, kdy a jak se funkce zavolá.
# 2) Napiš dekorátor, který změří čas, po který funkce pracuje a výsledek vypíše — také vhodné
# pro ladění, pokud nám přijde, že nějaká funkce trvá moc dlouho a chceme si to ověřit. Možno
# nakombinovat s prvním dekorátorem.
# 3) Napiš libovolný vlastní dekorátor.
# 4) Pokud ve funkci dojde k výjimce, dodá odkaz na google, který tu konkrétní chybu vyhledá.
# 5) Napiš dekorátor, který zakáže printy. Pokude bude dekorovaná funkce něco vypisovat printem,
# tento výpis se neukáže, ale funkce bude dále normálně fungovat a vracet výsledky.


def debug_message(func):
    """Task 1 a 2
       Decorator displays simple message with:
                  * function's name
                  * positional arguments
                  * keyword arguments
                  * elapsed time
    """
    import functools
    import time

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start

        template = f'''
        ============ DEBUG START ============
        Function's name: {func.__name__}
        Positional arguments: {args}
        Keyword arguments: {kwargs}
        Elapsed time: {end}
        ============ DEBUG END ==============
        '''

        print(template)
        return result

    return inner


def function_runned_count(func):
    """Task 3
       Decorator creates file with statistics -
       how many times was the function runned.
    """
    import functools
    import json

    @functools.wraps(func)
    def inner(*args, **kwargs):
        file = 'statistics.json'
        try:
            with open(file, mode='r') as s:
                db = json.load(s)
        except IOError:
            db = {}

        funcion_name = func.__name__
        if funcion_name in db:
            db[funcion_name] += 1
        else:
            db[funcion_name] = 1

        with open(file, mode='w') as s:
            s.write(json.dumps(db, ensure_ascii=False, indent=2))

        return func(*args, **kwargs)

    return inner


def seach_python_error(func):
    """Task 4
       If an error occurs in the program, the decorator opens the browser
       and starts looking for an error.
       The searched value is "Python" + Error name.
       """
    import functools
    import webbrowser

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            exception_name = type(ex).__name__
            url = 'https://www.google.com/search?q=Python+' + exception_name
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

    return inner


def without_print(func):
    """Task 5
       Decorator disables the "print" function inside functions.
       """
    import functools
    import sys

    @functools.wraps(func)
    def inner(*args, **kwargs):
        sys.stdout = None
        result = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return result
    return inner
