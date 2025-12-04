def main():
    zahlen = [1,2,3,4,5,6,7,8,9,10]
    #List Comprehension
    list_quadrate = [x * x for x in zahlen]
    print(list_quadrate)
    #Dict Comprehension
    dict_quadrate = {x: x*x for x in zahlen if x%2 == 0}
    print(dict_quadrate)
    #Set Comprehension
    set_quadrate = {"gerade" if x%2==0 else "ungerade" for x in zahlen}
    print(set_quadrate)

if __name__ == "__main__":
    main()