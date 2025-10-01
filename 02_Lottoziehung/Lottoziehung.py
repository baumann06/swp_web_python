import random

# Position 20 ziehen → Zahl von Pos 20 ans Ende verschieben
# Anzahl der noch ziehbaren Zahlen in der Liste um 1 verringern

def lottoziehung():
    zahlen = list(range(1, 46))
    gezogene_zahlen = []
    anzahl_ziehbar = len(zahlen)

    for i in range(6):
        pos = random.randint(0, anzahl_ziehbar-1)
        gezogene_zahlen.append(zahlen[pos])

        zahlen[pos], zahlen[anzahl_ziehbar-1] = zahlen[anzahl_ziehbar-1], zahlen[pos]

        anzahl_ziehbar -= 1
    print("Gezogene Zahlen:", gezogene_zahlen)
    return gezogene_zahlen

def statistik():
    d_statistik = dict.fromkeys(range(1,46),0)

    for i in range(1000):
        gezogene_zahlen = lottoziehung()
        for zahl in gezogene_zahlen:
            d_statistik.update({zahl : d_statistik.get(zahl) + 1})

    print(d_statistik)

def main():
    #lottoziehung()
    statistik()

if __name__ == "__main__":
    main()
