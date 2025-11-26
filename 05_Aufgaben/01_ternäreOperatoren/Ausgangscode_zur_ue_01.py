import random


def klassifiziere_zahl(zahl):
    if zahl < 0:
        klassifikation = "negativ"
    elif zahl == 0:
        klassifikation = "null"
    else:
        klassifikation = "positiv"

    return klassifikation


def ist_gerade(zahl):
    if zahl % 2 == 0:
        result = True
    else:
        result = False

    return result


def berechne_rabatt(preis, kundentyp):
    if kundentyp == "premium":
        rabatt = 0.2
    elif kundentyp == "standard":
        rabatt = 0.1
    else:
        rabatt = 0.0

    return preis * (1 - rabatt)


def bewerte_note(note):
    if note >= 90:
        bewertung = "Sehr gut"
    elif note >= 80:
        bewertung = "Gut"
    elif note >= 70:
        bewertung = "Befriedigend"
    elif note >= 60:
        bewertung = "Ausreichend"
    else:
        bewertung = "Mangelhaft"

    return bewertung


def altersgruppe(alter):
    if alter < 13:
        gruppe = "Kind"
    elif alter < 18:
        gruppe = "Jugendlicher"
    elif alter < 65:
        gruppe = "Erwachsener"
    else:
        gruppe = "Senior"

    return gruppe


def verkehrsamel(geschwindigkeit, limit):
    if geschwindigkeit <= limit:
        status = "OK"
    else:
        status = "Zu schnell"

    return status


# List Comprehension mit Ternary Operator
def markiere_zahlen(zahlen):
    result = []
    for zahl in zahlen:
        if zahl % 2 == 0:
            result.append("gerade")
        else:
            result.append("ungerade")
    return result


# Tuple Indexing Method
def finde_groessere(a, b):
    if a > b:
        result = a
    else:
        result = b
    return result


# Dictionary Method
def waehle_rabatt_typ(betrag):
    if betrag > 100:
        rabatt_typ = "Rabatt"
    else:
        rabatt_typ = "Kein Rabatt"
    return rabatt_typ


# Print mit Ternary Operator
def vergleiche_und_drucke(a, b):
    if a > b:
        print("a ist größer")
    else:
        print("b ist größer")


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
    print("finde_maximum(7, 12):", finde_maximum(7, 12))
    print("vergleiche_und_drucke(5, 15):")
    vergleiche_und_drucke(5, 15)


if __name__ == "__main__":
    main()