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


class Karte:
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]
    FARBEN = ["Kreuz", "Pik", "Herz", "Karo"]

    def __init__(self, value_index, farben_index):
        self.value = self.VALUES[value_index]
        self.farbe = self.FARBEN[farben_index]
        self.value_index = value_index  # für vergleiche (0-12)

    def __repr__(self):
        return f"{self.value} {self.farbe[:5]}"


def erstelle_alle_karten():
    karten = []
    for farben_index in range(4):
        for value_index in range(13):
            karten.append(Karte(value_index, farben_index))
    return karten


def flush(gezogen):
    farben = set()
    for karte in gezogen:
        farben.add(karte.farbe)
    if len(farben) == 1:
        return True
    return False


def pair(gezogen):
    values = [karte.value_index for karte in gezogen]
    pair_count = 0

    for value in values:
        if values.count(value) == 2:
            pair_count += 1

    pair_count = pair_count // 2

    if pair_count == 1:
        return "one pair"
    elif pair_count == 2:
        return "two pair"
    else:
        return False


def drillinge(gezogen):
    values = [karte.value_index for karte in gezogen]
    for value in values:
        if values.count(value) == 3:
            return True
    return False


def vierling(gezogen):
    values = [karte.value_index for karte in gezogen]
    for value in values:
        if values.count(value) == 4:
            return True
    return False


def strasse(gezogen):
    values = sorted([karte.value_index for karte in gezogen])

    # normale strasse
    if values[4] - values[0] == 4 and len(set(values)) == 5:
        return True

    # strasse übers eck (A-2-3-4-5): [0,1,2,3,12]
    if values == [0, 1, 2, 3, 12]:
        return True

    return False


def main():
    deck = erstelle_alle_karten()

    # ziehe 5 zufällige karten
    gezogen = random.sample(deck, 5)

    print("Gezogene Karten: ", gezogen)
    print()
    print("Flush: ", flush(gezogen))
    print("Paar: ", pair(gezogen))
    print("Drillinge: ", drillinge(gezogen))
    print("Vierling: ", vierling(gezogen))
    print("Strasse: ", strasse(gezogen))


if __name__ == "__main__":
    main()