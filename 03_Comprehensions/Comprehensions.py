def listComprehension(zahlen):
    list_comp = [x * x for x in zahlen]
    print(list_comp)

def dictComprehension(zahlen):
    dict_comp = {x: x * x for x in zahlen if x % 2 == 0}
    print(dict_comp)

def setComprehension(zahlen):
    set_comp = {"gerade" if x % 2 == 0 else "ungerade" for x in zahlen}
    print(set_comp)

def main():
    zahlen = [1,2,3,4,5,6,7,8,9,10]
    #List Comprehension
    listComprehension(zahlen)
    #Dict Comprehension
    dictComprehension(zahlen)
    #Set Comprehension
    setComprehension(zahlen)

if __name__ == "__main__":
    main()