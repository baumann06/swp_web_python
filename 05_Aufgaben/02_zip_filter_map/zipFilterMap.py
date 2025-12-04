def combineThreeLists(a: list, b: list, c: list):
    combined = list(zip(a, b, c))
    return combined

def main():
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]

    personen = combineThreeLists(names, ages, scores)

    filteredPersons = list(filter(lambda x: True if x[1] >= 18 and x[2] >= 80 else False, personen))

    mapPersons = list(map(lambda x: {"name": x[0], "age": x[1], "score": x[2]}, filteredPersons))

    print(mapPersons)

if __name__ == '__main__':
    main()