class Firma:

    def __init__(self, firmenname):
        self.firmenname = firmenname
        self.abteilungen = []

    def __str__(self):
        return f"Firmenname: {self.firmenname}"

    def anzahlAbteilungen(self):
        return len(self.abteilungen)

    def addAbteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def removeAbteilung(self, abteilung):
        if(abteilung in self.abteilungen):
            self.abteilungen.remove(abteilung)
            return True
        return False

    def removeByIdAbteilung(self, abteilungsId):
        for abteilung in self.abteilungen:
            if abteilung.abteilungsId == abteilungsId:
                self.abteilungen.remove(abteilung)
                return True
        return False

    def anzahlMitarbeiter(self):
        mitarbeiterCount = 0
        for abteilung in self.abteilungen:
            mitarbeiterCount += len(abteilung.mitarbeiter)
        return mitarbeiterCount

    def anzahlAbteilungsleiter(self):
        abteilungsleiterCount = 0
        for abteilung in self.abteilungen:
            if abteilung.abteilungsleiter:
                abteilungsleiterCount += 1
        return abteilungsleiterCount


    def maxAbteilung(self):
        if not self.abteilungen:
            return None

        groessteAbteilung = self.abteilungen[0]
        for abteilung in self.abteilungen:
            if len(groessteAbteilung.mitarbeiter) < len(abteilung.mitarbeiter):
                groessteAbteilung = abteilung
        return groessteAbteilung

    def anzahlMaenner(self):
        mitarbeiterCount = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == mitarbeiter.MAENNLICH:
                    mitarbeiterCount += 1
        return mitarbeiterCount

    def anzahlFrauen(self):
        mitarbeiterCount = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == mitarbeiter.WEIBLICH:
                    mitarbeiterCount += 1
        return mitarbeiterCount

    def anteilFrauenProzent(self):
        prozent =  (self.anzahlFrauen() / self.anzahlMitarbeiter()) *100
        return round(prozent,2)

    def anteilMaennerProzent(self):
        prozent = (self.anzahlMaenner() / self.anzahlMitarbeiter())*100
        return round(prozent,2)