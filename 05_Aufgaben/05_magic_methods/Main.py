from Auto import Auto

def main():
    a1 = Auto(60)
    a2 = Auto(50)

    print(a1)
    print(len(a1))
    print(a1 + a2)
    print(a2 - a1)
    print(a1 * a2)

    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)


if __name__ == '__main__':
    main()