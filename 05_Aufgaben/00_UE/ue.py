import random
from unittest import case


def main():

# dict Datum Messwert
    a = list(range(11))
    print(a)

    d = {"12.11": 12, "12.02.": 13, "11.01": 12}
    print(d)
    # print(d.values())
    # print(d.items())
    # print(d.keys())

    for temp in set(d.values()):
        tage = [tag for tag, wert in d.items() if wert == temp]
        if len(tage) == 2:
            print("gleiche Temp an", tage)

# Poker
    k = list(range(52))

    k_farbe = [k // 13 for k in k]
    print(k_farbe)
    k_zahl = [k % 13 for k in k]
    print(k_zahl)

    gezogene = random.sample(k, 5)

    gezogene.sort()

    # Farbe und Wert für gezogene Karten bestimmen
    gezogene_farben = [k_farbe[i] for i in gezogene]
    gezogene_werte  = [k_zahl[i] for i in gezogene]

    print("Gezogene Karten:", gezogene)
    print("Farben:", gezogene_farben)
    print("Werte:", gezogene_werte)

    # Doppelte Farben prüfen
    for farbe in set(gezogene_farben):
        if gezogene_farben.count(farbe) == 2:
            print(f"Zwei gleiche Farben: {farbe}")

    # Doppelte Werte prüfen
    for wert in set(gezogene_werte):
        if gezogene_werte.count(wert) == 2:
            print(f"Zwei gleiche Werte: {wert}")

# Lotto
    print("Lotto ------------")
    #zahlen = lottoziehung(45, 6)
    #print(zahlen)
    stats = statistik( 45, 10000)
    print(stats)


    alter = 20
    freigabe = "Kind" if alter < 13 else "Tennager" if alter < 18 else "Erwachsener" if alter < 65 else "Senior"
    print(freigabe)

    farbe = "rot"
    match farbe:
        case "blau":
            print("Blau")
        case "gelb":
            print("Gelb")
        case "rot":
            print("Rot")
        case _:
            print("nicht gefunden")

    b = [1,2,2,3,4,4]
    print(b)
    for x in set(b):
        if b.count(x) == 2:
            print("doppelt", x)

    z = [x for x in set(b) if b.count(x) ==2]
    print(z)
    print(z[1])


def lottoziehung(ende, anzahl):
    import random
    zahlenZiehbar = list(range(1, ende + 1))
    random.shuffle(zahlenZiehbar)
    gezogen = zahlenZiehbar[:anzahl]
    return gezogen

def statistik(ende, ziehungen):
    d = {zahl: 0 for zahl in range(1, ende+1)}

    for _ in range(ziehungen):
        zahlen = lottoziehung(45, 6)
        for zahl in zahlen:
            d[zahl] += 1

    return d

if __name__ == '__main__':
    main()

