from Firma import Firma
from Abteilung import Abteilung
from Mitarbeiter import Mitarbeiter
from Abteilungsleiter import Abteilungsleiter

def main():
    firma = Firma("XXX")

    it = Abteilung(0, "IT", )
    hr = Abteilung(1, "HR", )

    firma.addAbteilung(it)
    firma.addAbteilung(hr)

    m1 = Mitarbeiter(0, "Franz", "Josef", "m", 35)
    m2 = Mitarbeiter(1, "Manfred", "Unterer", "m", 45)
    m3 = Mitarbeiter(2, "Laura", "Oberer", "w", 76)

    m4 = Mitarbeiter(3, "Lisa", "Moser", "w", 23)
    m5 = Mitarbeiter(4, "Mona", "Jung", "w", 34)
    m6 = Mitarbeiter(5, "Georg", "Alt", "m", 55)

    it.addMitarbeiter(m1)
    it.addMitarbeiter(m2)
    it.addMitarbeiter(m3)

    hr.addMitarbeiter(m4)
    hr.addMitarbeiter(m5)
    hr.addMitarbeiter(m6)

    leiter = Abteilungsleiter("Johann", "Neumann", 7, "m", 44)

    it.setAbteilungsleiter(leiter)


    print("Anzahl Abteilungen: "+str(firma.anzahlAbteilungen()))
    print("Anzahl Abteilungsleiter: "+str(firma.anzahlAbteilungsleiter()))

    print("Anzahl Mitarbeiter: "+str(firma.anzahlMitarbeiter()))
    print("Größte Abteilung: "+str(firma.maxAbteilung()))

    print("Prozentanteil Frauen: "+str(firma.anteilFrauenProzent())+"%")
    print("Prozentanteil Männer: "+str(firma.anteilMaennerProzent())+"%")

if __name__ == "__main__":
    main()