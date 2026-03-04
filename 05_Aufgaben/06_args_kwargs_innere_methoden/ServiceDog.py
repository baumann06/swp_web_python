from Dog import Dog

class ServiceDog(Dog):
    def __init__(self, name, breed, task):
        self.task = task
        super().__init__(name, breed)

    def __str__(self):
        return f"{super().__str__()} mit der Aufgabe {self.task}"