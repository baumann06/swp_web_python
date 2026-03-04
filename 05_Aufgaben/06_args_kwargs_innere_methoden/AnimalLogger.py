class AnimalLogger:
    def __enter__(self):
        print("Logger geöffnet")
        return self

    def __exit__(self):
        print("Logger geschlossen")
        return None

    def log(self, animal):
        print(animal)