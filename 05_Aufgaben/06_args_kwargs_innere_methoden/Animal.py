class Animal:
    species = 'Unknown'
    count = 0
    _next_id = 1

    def __init__(self, name):
        self.name = name
        Animal.count += 1
        self.__id = Animal._next_id
        Animal._next_id += 1

    def __str__(self):
        return f"{self.name} {self.__id}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def describe():
        return f"Das ist ein Tier"