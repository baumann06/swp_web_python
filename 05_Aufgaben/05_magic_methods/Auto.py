class Auto():
    def __init__(self, ps):
        self.ps = ps

    def __str__(self):
        return f"Auto mit {self.ps} PS."

    def __len__(self):
        return self.ps

    def __add__(self, other):
        return self.ps + other.ps

    def __sub__(self, other):
        return self.ps - other.ps

    def __mul__(self, other):
        return self.ps * other.ps

    def __eq__(self, other):
        return self.ps == other.ps

    def __lt__(self, other):
        return self.ps < other.ps

    def __gt__(self, other):
        return self.ps > other.ps