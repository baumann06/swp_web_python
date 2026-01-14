from Personen import Personen

class Mitarbeiter(Personen):
    def __init__(self, mitarbeiterId, vorname, nachname, geschlecht, alter):
        self.mitarbeiterId = mitarbeiterId
        self.abteilung = None

        super().__init__(vorname, nachname, geschlecht, alter)


    def __str__(self):
        return f"Mitarbeiter {super().__str__()} Hat die Mitarbeiter ID {self.mitarbeiterId}."

