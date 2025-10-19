# Dict Comprehension mit Buchstaben A–Z als Schlüssel und ihrer Position im Alphabet (1–26) als Werte erstellen.

# chr(65) -> A
# ord(A) -> 65


def dictComprehension(buchstaben):
    dict_comp = {b: ord(b)-64 for b in buchstaben}
    print(dict_comp)

def main():
    buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    dictComprehension(buchstaben)

if __name__ == "__main__":
    main()