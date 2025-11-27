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

# Ternärer Operator in Zeile 55
# Dict-Ternär Zeile 44
import random
import unittest

class Karte:
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]
    FARBEN = ["Kreuz", "Pik", "Herz", "Karo"]

    def __init__(self, value_index, farben_index):
        self.value = self.VALUES[value_index]
        self.farbe = self.FARBEN[farben_index]
        self.value_index = value_index  # für vergleiche (0-12)

    def __repr__(self):
        return f"{self.value} {self.farbe[:5]}"


def erstelleAlleKarten():
    karten = []
    for farben_index in range(4):
        for value_index in range(13):
            karten.append(Karte(value_index, farben_index))
    return karten


def flush(gezogen):
    farben = set()
    for karte in gezogen:
        farben.add(karte.farbe)

    # Dict-Ternär
    return {True: True, False: False}[len(farben) == 1]

def pair(gezogen):
    values = [karte.value_index for karte in gezogen]
    pair_count = 0

    for value in values:
        if values.count(value) == 2:
            pair_count += 1

    pair_count = pair_count // 2

    # Ternärer Operator mit if-else
    return "two pair" if pair_count == 2 else "one pair" if pair_count == 1 else False

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

    # strasse übers Eck (A-2-3-4-5): [0,1,2,3,12]
    if values == [0, 1, 2, 3, 12]:
        return True

    return False


def royalFlush(gezogen):
    values = sorted([karte.value_index for karte in gezogen])

    if values == [8, 9, 10, 11, 12]:
        return True

    return False


def full_house(gezogen):
    values = [karte.value_index for karte in gezogen]
    counts = {}

    for value in values:
        counts[value] = values.count(value)

    # Full House = 3 gleiche + 2 gleiche
    if sorted(counts.values()) == [2, 3]:
        return True
    return False


def identifiziere_kombination(gezogen):
    # Unwahrscheinlichste zuerst
    if flush(gezogen) and royalFlush(gezogen):
        return "Royal Flush"
    if vierling(gezogen):
        return "Vierling"
    if full_house(gezogen):
        return "Full House"
    if flush(gezogen) and strasse(gezogen):
        return "Straight Flush"
    if flush(gezogen):
        return "Flush"
    if strasse(gezogen):
        return "Strasse"
    if drillinge(gezogen):
        return "Drillinge"

    pair_result = pair(gezogen)
    if pair_result:
        return pair_result

    return "Höchste Karte"


def simuliere(x):
    # spielt 100.000 Mal und zählt die Kombinationen
    deck = erstelleAlleKarten()
    kombinationen = {}

    for _ in range(x):
        gezogen = random.sample(deck, 5)
        kombi = identifiziere_kombination(gezogen)

        if kombi not in kombinationen:
            kombinationen[kombi] = 0
        kombinationen[kombi] += 1

    return kombinationen


def statistik(kombinationen, x):
    # Statistik mit prozentuellen Anteilen
    total = sum(kombinationen.values())
    prozentsatze = [50.13, 42.25, 4.75, 2.11, 0.39, 0.20, 0.14, 0.02, 0.00135, 0.00015]

    print(f"\n{'Kombination':<20} {'Anzahl':<10} {'Prozent':<20} {'Relative Abweichung':20}")

    # Sortiere nach Häufigkeit (absteigend)
    for i, (kombi, count) in enumerate(sorted(kombinationen.items(), key=lambda x: x[1], reverse=True)):
        prozent = (count / total) * 100

        relativProzent = (prozentsatze[i] - prozent) / prozent

        print(f"{kombi:<20} {count:<10} {prozent:>10f}% {relativProzent:>20f}%")

    print(f"{'TOTAL':<20} {total:<10}")


def main():
    x = 100000
    print(f"Simuliere {x} Pokerspiele...")
    kombinationen = simuliere(x)
    statistik(kombinationen, x)

class TestPoker(unittest.TestCase):
    def testFlush(self):
        karten = [Karte(12,0), Karte(5,0), Karte(2, 0), Karte(0, 0), Karte(7,0)]
        self.assertTrue(flush(karten),"Fehler")

        karten = [Karte(12,2), Karte(5,1), Karte(2, 0), Karte(0, 0), Karte(7,0)]
        self.assertFalse(flush(karten), "Fehler")

    def testPair(self):
        karten = [Karte(0, 0), Karte(0, 1), Karte(2, 0), Karte(3, 0), Karte(4, 0)]
        self.assertEqual(pair(karten), "one pair")

        karten = [Karte(0, 0), Karte(0, 1), Karte(2, 0), Karte(2, 1), Karte(4, 0)]
        self.assertEqual(pair(karten), "two pair")

    def test_strasse(self):
        karten = [Karte(0, 0), Karte(1, 1), Karte(2, 2), Karte(3, 3), Karte(4, 0)]
        self.assertTrue(strasse(karten))

    def test_full_house(self):
        # Test (3+2)
        karten = [Karte(0, 0), Karte(0, 1), Karte(0, 2), Karte(1, 0), Karte(1, 1)]
        self.assertTrue(full_house(karten))

if __name__ == "__main__":
    unittest.main(exit=False)
    main()