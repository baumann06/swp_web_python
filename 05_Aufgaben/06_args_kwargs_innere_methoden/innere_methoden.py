# Schreibe eine Funktion multiply_by(n), die eine Funktion zurückgibt.

# Die zurückgegebene Funktion soll eine Zahl mit n multiplizieren.


def multiply_by(n):
    def multiply(x):
        return x * n
    return multiply

def main():
    double = multiply_by(2)
    print(double(5))  # 10

    triple = multiply_by(3)
    print(triple(5))  # 15

if __name__ == '__main__':
    main()