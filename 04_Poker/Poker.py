# liste 52 Zahlen
# floor divison
# modulo 13 um aufs symbol zu kommen
# 5 int alle Farben ausrechen (durch 13)
# Symbole modulo 13
# set auf 5 karten dann sind sie von gleicher farbe
# paar for Schleife äußere von 0-vorletzte
# drillinge counter
# straße aufsteigend
# flush + straße = royal flush
# unwahrscheinlichste zuerst wahrscheinlichste zuletzt
# Straße übers Eck dabei oder nicht ausprobieren
import random

def flush(gezogen):
    farben = set()
    for i in gezogen:
        farben.add(i // 13)
    if len(farben) == 1:
        return True
    return False


def pair(gezogen):
    symbole = [karte % 13 for karte in gezogen]
    pair_count = 0

    for symbol in symbole:
        if symbole.count(symbol) == 2:
            pair_count += 1

    pair_count = pair_count // 2

    if pair_count == 1:
        return "one pair"
    elif pair_count == 2:
        return "two pair"
    else:
        return False

def drillinge(gezogen):
    symbole = [karte % 13 for karte in gezogen]
    for symbol in symbole:
        if symbole.count(symbol) == 3:
            return True
    return False

def vierling(gezogen):
    symbole = [karte % 13 for karte in gezogen]
    for symbol in symbole:
        if symbole.count(symbol) == 4:
            return True
    return False

def colors(gezogen):
    color = set()
    for i in gezogen:
        color.add(i // 13)
    print(color)
    return len(color)


def strasse(gezogen):
    symbole = sorted([karte % 13 for karte in gezogen])

    # normale strasse
    if symbole[4] - symbole[0] == 4 and len(set(symbole)) == 5:
        return True

    # strasse übers Eck (A-2-3-4-5)
    if symbole == [0, 1, 2, 3, 12]:
        return True

    return False

def main():
    karten = range(0,52)
    gezogen = []
    for i in range(5):
        gezogen.append(random.choice(karten))

    gezogen.sort()
    print(gezogen)

    print("Flush: ", flush(gezogen))
    print("Paar: ", pair(gezogen))
    print("Drillinge: ", drillinge(gezogen))
    print("Vierling: ", vierling(gezogen))
    print("Strasse: ", strasse(gezogen))


if __name__ == "__main__":
    main()