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


def debug_vypis(func):
    """Úkol 1 a 2
       Dekorátor vypíše jednoduchou zprávu, která obsahuje název volané funkce,
       vložené hodnoty pozičních argumentů, pojmenovaných argumentů a
       nakonec čas, který funkce spotřebovala.
    """
    import functools
    import time

    @functools.wraps(func)
    def nahradni_funkce(*args, **kwargs):
        start = time.time()
        vysledek = func(*args, **kwargs)
        end = time.time() - start

        sablona = f'''
        ============ DEBUG START ============
        Název volané funkce: {func.__name__}
        Poziční argumenty: {args}
        Pojmenované argumenty: {kwargs}
        Čas trvání funkce: {end}
        ============ DEBUG END ==============
        '''

        print(sablona)
        return vysledek

    return nahradni_funkce


def pocet_spusteni_funkce(func):
    """Úkol 3
       Dekorátor vytvoří soubor se statistikou,
       kolikrát byla funkce spuštěna."""
    import functools
    import json

    @functools.wraps(func)
    def nahradni_funkce(*args, **kwargs):
        soubor = 'statistika.json'
        try:
            with open(soubor, mode='r') as s:
                databaze = json.load(s)
        except IOError:
            databaze = {}

        funkce = func.__name__
        if funkce in databaze:
            databaze[funkce] += 1
        else:
            databaze[funkce] = 1

        with open(soubor, mode='w') as s:
            s.write(json.dumps(databaze, ensure_ascii=False, indent=2))

        return func(*args, **kwargs)

    return nahradni_funkce


def seach_python_error(func):
    """Úkol 4
       Pokud v programu dojde k chybě, dekorátor otevře prohlížeč
       a začne hledat chybu. Hledané spojení je "Python" +
       název chyby.
       """
    import functools
    import webbrowser

    @functools.wraps(func)
    def nahradni_funkce(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            vyjimka = type(ex).__name__
            url = 'https://www.google.com/search?q=Python+' + vyjimka
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

    return nahradni_funkce


def bez_printu(func):
    """Úkol 5
       Dekorátor, který zakazuje printy uvnitř funkce.
       """
    import functools
    import sys

    @functools.wraps(func)
    def nahradni_funkce(*args, **kwargs):
        sys.stdout = None
        vysledek = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return vysledek
    return nahradni_funkce
