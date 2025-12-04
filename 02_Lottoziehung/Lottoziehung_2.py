import random

def lottoziehung(start, ende, anzahl):
    zahlen = list(range(start + 1, ende + 1))
    gezogene_zahlen = []
    anzahl_ziehbar = len(zahlen)

    for _ in range(anzahl):
        pos = random.randint(0, anzahl_ziehbar - 1)
        gezogene_zahlen.append(zahlen[pos])
        zahlen[pos], zahlen[anzahl_ziehbar - 1] = zahlen[anzahl_ziehbar - 1], zahlen[pos]
        anzahl_ziehbar -= 1

    return gezogene_zahlen

def statistik(start, ende, anzahl, durchlaeufe):
    d_statistik = dict.fromkeys(range(start + 1, ende + 1), 0)
    for _ in range(durchlaeufe):
        gezogene_zahlen = lottoziehung(start, ende, anzahl)
        for zahl in gezogene_zahlen:
            d_statistik[zahl] += 1
    return d_statistik

def main():
    start = 0
    ende = 45
    anzahl = 6
    durchlaeufe = 1000

    ergebnis = statistik(start, ende, anzahl, durchlaeufe)
    print(ergebnis)

if __name__ == "__main__":
    main()
