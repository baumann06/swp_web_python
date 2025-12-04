import random

def liste():
    l = []
    for _ in range(20):
        l.append(random.randint(5000, 100001))

    l.sort()
    print("Zufall", l)
    return l

def steuersatz(x):
    steuer = 0
    if x <= 10000:
        steuer = 40
    elif 10000 < x <= 30000:
        steuer = 55
    elif 30000 < x <= 70000:
        steuer = 75
    elif x > 70000:
        steuer = 82

    return steuer

def main():
    l = liste()
    gruppe = {"40%_Steuer":0, "55%Steuer":0, "75%Steuer":0, "82%Steuer":0}
    for i in range(len(l)):
        if(steuersatz(l[i]) == 40):
            gruppe["40%_Steuer"] += 1
        elif(steuersatz(l[i]) == 55):
            gruppe["55%Steuer"] += 1
        elif(steuersatz(l[i]) == 75):
            gruppe["75%Steuer"] += 1
        elif(steuersatz(l[i]) == 82):
            gruppe["82%Steuer"] += 1

    print("Dict", gruppe)

if __name__ == "__main__":
    main()