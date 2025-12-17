from Firma import Firma

class Abteilung(Firma):

    def __init__(self, firmenname, standort, abteilungs_id, abteilungsname):
        super().__init__(firmenname, standort)

        self.abteilungs_id = abteilungs_id
        self.abteilungsname = abteilungsname

    def __str__(self):
        return f"{super().__str__()}, Abteilung: {self.abteilungsname} (ID {self.abteilungs_id})"

