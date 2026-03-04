class AnimalShelter:
    def __init__(self, animals=None):
        self.animals = animals if animals is not None else []
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.animals):
            animal = self.animals[self._index]
            self._index += 1
            return animal
        else:
            raise StopIteration  # Ende der Iteration
