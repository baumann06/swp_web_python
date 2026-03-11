from Knoten import Knoten
from LinkedList import LinkedList
import random

def main():
    liste = LinkedList()

    for i in range(10):
        zahl = random.randint(1,100)
        liste.append(zahl)

    liste.print_list()
    print()
    print(liste.length())

    x=1
    for y in liste:
        print(f"Element {x}: {y}")
        x = x+1

if __name__ == '__main__':
    main()