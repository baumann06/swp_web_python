import random


def klassifiziere_zahl(zahl):
    klassifikation = "negativ" if zahl < 0 else "null" if zahl == 0 else "positiv"
    return klassifikation

def ist_gerade(zahl):
    result = True if zahl % 2 == 0 else False
    return result


def berechne_rabatt(preis, kundentyp):
    rabatt = 0.2 if kundentyp == "premium" else 0.1 if kundentyp == "standard" else 0.0
    return preis * (1 - rabatt)


def bewerte_note(note):
    bewertung = "Sehr gut" if note >= 90 else "Gut" if note >= 80 else "Befriedigend" if note >= 70 else "Ausreichend" if note >= 60 else "Mangelhaft"
    return bewertung


def altersgruppe(alter):
    gruppe = "Kind" if alter < 13 else "Jugendlicher" if alter < 18 else "Erwachsener" if alter < 65 else "Senior"
    return gruppe


def verkehrsamel(geschwindigkeit, limit):
    status = "OK" if geschwindigkeit <= limit else "Zu schnell"
    return status


# List Comprehension mit Ternary Operator
def markiere_zahlen(zahlen):
    result = ["gerade" if zahl % 2 == 0 else "ungerade" for zahl in zahlen]
    return result


# Tuple Indexing Method
def finde_groessere(a, b):
    result = (b,a)[a>b]
    return result


# Dictionary Method
def waehle_rabatt_typ(betrag):
    rabatt_typ = {True: "Rabatt", False: "Kein Rabatt"}[betrag > 100]
    return rabatt_typ

# Print mit Ternary Operator
def vergleiche_und_drucke(a, b):
    print("a ist größer" if a > b else "b ist größer")


def main():
    # Test klassifiziere_zahl
    print("klassifiziere_zahl(-5):", klassifiziere_zahl(-5))
    print("ist_gerade(4):", ist_gerade(4))
    print("berechne_rabatt(100, 'premium'):", berechne_rabatt(100, "premium"))
    print("bewerte_note(85):", bewerte_note(85))
    print("altersgruppe(25):", altersgruppe(25))
    print("verkehrsamel(60, 50):", verkehrsamel(60, 50))

    # Test neue Funktionen (zum Üben)
    print("\n--- Übungen ---")
    print("markiere_zahlen([1, 2, 3, 4, 5]):", markiere_zahlen([1, 2, 3, 4, 5]))
    print("finde_groessere(10, 20):", finde_groessere(10, 20))
    print("waehle_rabatt_typ(150):", waehle_rabatt_typ(150))
    print("vergleiche_und_drucke(5, 15):")
    vergleiche_und_drucke(5, 15)


if __name__ == "__main__":
    main()