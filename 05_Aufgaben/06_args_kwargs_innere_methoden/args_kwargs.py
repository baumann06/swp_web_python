# *args	Alle Positionsargumente als Tupel
# **kwargs	Alle benannten Argumente als Dictionary

# Schreibe einen Decorator repeat, der eine Funktion zweimal ausführt.

def repeat(func):

    # man braucht beides args und kwargs weil eine Funktion so aussehen kann: func(1, 2, x=5, y=7)
    # kwargs sammelt benannte argumente als dict und args als tuppel
    # args = (1, 2)
    # kwargs = {'x': 5, 'y': 7}
    # wenn man beides schreibt ist es egal wie die Orginalfunktion ausschaut es wird alles weitergeleitet

    def repeater(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return repeater

def say_hello(name):
    print(f"Hallo {name}")

def main():
    new_say_hello = repeat(say_hello)
    new_say_hello("Bruno")

if __name__ == '__main__':
    main()