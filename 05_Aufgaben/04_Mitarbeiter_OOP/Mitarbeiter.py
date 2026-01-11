class Mitarbeiter():
    MAENNLICH = "m"
    WEIBLICH = "w"

    def __init__(self, mitarbeiterId, vorname, nachname, geschlecht, alter):
        self.mitarbeiterId = mitarbeiterId
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.abteilung = None

        if geschlecht not in (Mitarbeiter.MAENNLICH, Mitarbeiter.WEIBLICH):
            raise ValueError("Geschlecht muss m oder w sein")
        self.geschlecht = geschlecht


    def __str__(self):
        return (f"Mitarbeiter {self.vorname} {self.nachname} "
                f"mit der Id {self.mitarbeiterId} ist {self.geschlecht} "
                f"und {self.alter} alt.")

