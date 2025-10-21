# Dict Comprehension mit Buchstaben A–Z als Schlüssel und ihrer Position im Alphabet (1–26) als Werte erstellen.

# chr(65) -> A
# ord(A) -> 65

import string

def dictComprehension(buchstaben):
    dict_comp = {b: ord(b) - 64 for b in buchstaben}
    print(dict_comp)

def main():
    buchstaben = string.ascii_uppercase
    dictComprehension(buchstaben)

if __name__ == "__main__":
    main()
