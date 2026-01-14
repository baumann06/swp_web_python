class Personen:
    MAENNLICH = "m"
    WEIBLICH = "w"

    def __init__(self, vorname, nachname, geschlecht, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter

        if geschlecht not in (Personen.MAENNLICH, Personen.WEIBLICH):
            raise ValueError("Geschlecht muss m oder w sein")
        self.geschlecht = geschlecht

    def __str__(self):
        return f"{self.vorname} {self.nachname} ist {self.geschlecht} und {self.alter} Jahre alt."