class Abteilung():

    def __init__(self, abteilungsId, abteilungsname, abteilungsleiter=None):
        self.abteilungsId = abteilungsId
        self.abteilungsname = abteilungsname
        self.abteilungsleiter = abteilungsleiter
        self.mitarbeiter = []

        if abteilungsleiter is not None:
            self.addMitarbeiter(abteilungsleiter)


    def __str__(self):
        return (f"Die Abteilung "
                f"{self.abteilungsname} hat die ID: {self.abteilungsId} und {len(self.mitarbeiter)} Mitarbeiter."
                f" Der Leiter dieser Abteilung heißt {self.abteilungsleiter}")

    def addMitarbeiter(self, mitarbeiter):
        if mitarbeiter.abteilung == None:
            mitarbeiter.abteilung = self
            self.mitarbeiter.append(mitarbeiter)
            return True
        return False

    def removeMitarbeiter(self, mitarbeiter):
        if(mitarbeiter in self.mitarbeiter):
            mitarbeiter.abteilung = None
            self.mitarbeiter.remove(mitarbeiter)
            return True
        return False

    def removeMitarbeiterbyId(self, mitarbeiterId):
        for mitarbeiter in self.mitarbeiter:
            if mitarbeiter.mitarbeiterId == mitarbeiterId:
                mitarbeiter.abteilung = None
                self.mitarbeiter.remove(mitarbeiter)
                return True
        return False

    def setAbteilungsleiter(self, abteilungsleiter):
        if self.abteilungsleiter in self.mitarbeiter:
            self.removeMitarbeiter(self.abteilungsleiter)

        self.abteilungsleiter = abteilungsleiter
        self.addMitarbeiter(abteilungsleiter)

    def getAbteilungsleiter(self):
        return (f"{self.abteilungsleiter.vorname} {self.abteilungsleiter.nachname} "
                f"mit der MitarbeiterId: {self.abteilungsleiter.mitarbeiterId}")

    def anzahlMitarbeiter(self):
        return len(self.mitarbeiter)