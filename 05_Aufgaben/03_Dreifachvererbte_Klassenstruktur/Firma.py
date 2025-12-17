class Firma:

    def __init__(self, firmenname, standort):
        self.firmenname = firmenname
        self.standort = standort

    def __str__(self):
        return f"Firma: {self.firmenname}, Standort: {self.standort}"