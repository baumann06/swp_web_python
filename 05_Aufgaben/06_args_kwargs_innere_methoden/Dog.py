from Animal import Animal

class Dog(Animal):

    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

    def __str__(self):
        return f"{super().__str__()} von der Rasse {self.breed}"


