from Mitarbeiter import Mitarbeiter

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, vorname, nachname, mitarbeiterId, geschlecht, alter):
        super().__init__(mitarbeiterId, vorname, nachname, geschlecht, alter)

    def __str__(self):
        if self.abteilung:
            return (f"{super().__str__()} {self.abteilung.abteilungsname} "
                    f"mit der ID {self.abteilung.abteilungsId} ")

        return (f"Abteilungsleiter ohne Abteilung."
                    f"{super().__str__()}")
