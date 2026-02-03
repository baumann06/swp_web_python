class Auto():
    def __init__(self, ps):
        self.ps = ps

    def __str__(self):
        return f"Auto mit {self.ps} PS."

    def __len__(self):
        return self.ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            raise TypeError("Muss vom Typ Auto sein")