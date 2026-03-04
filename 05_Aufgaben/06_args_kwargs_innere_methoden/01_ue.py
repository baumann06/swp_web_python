"""t = {2,4,4,4,5,}
print(t)
a=10
b=20
add = lambda a,b: a+b
print(add(10,20))

# Stern erzwingt benannte Übergabe
def testting(*, c, d):
    print(c+d)

testting(c=10, d=20)

class Eltern:

    def __init__(self, mutter, vater):
        self.mutter = mutter
        self.vater = vater

    def __str__(self):
        return f"{self.mutter} {self.vater}"

class Kind(Eltern):
    __anzahlKinder = 0
    def __init__(self, mutter, vater, name):
        super().__init__(mutter, vater)
        self.name = name
        Kind.__anzahlKinder += 1

    def __str__(self):
        return f"{self.name} {self.mutter} {self.vater}"


kinder = [Kind("Elsa", "Heinrich", "Josef"), Kind("Maria", "Josef", "Jesus")]
x = list(map(lambda k: k.name, kinder))
print(x)

f = Kind._Kind__anzahlKinder
print(f)

x = Kind("Lisa", "Markus", "Lion")
x.gausch = "Hallo"
print(x.gausch)
print(x)

#print(dir(...))

m = 30
def fu():
    print(m)  # Global
fu()

print(globals())
"""
from Animal import Animal
from ServiceDog import ServiceDog
from AnimalShelter import AnimalShelter
from Dog import Dog
from decorator import log_call
from decorator import repeat



x = ServiceDog("Joy", "GoldenRetriever", "Alltagshelfer")
print(x)

fido = Animal("Fido")

# Direkter Zugriff schlägt fehl
try:
    print(fido._Animal__id)
except AttributeError as e:
    print("Fehler:", e)

def create_animals(*args, **kwargs):
    animals = []
    for name in args:
        animals.append(Dog(name, "Unknown"))

    for name, breed in kwargs.items():
        animals.append(Dog(name, breed))

    return animals


@repeat(5)
def testing(c, d):
    print(c+d)

ani = create_animals()

testing(10,20)

def do_twice(func):
    def double(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return double


testing = do_twice(testing)

testing(56,20)


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

d = print(D.__mro__)






