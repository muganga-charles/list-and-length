def entry():
    number=int(input("how many elements are you entering"))
    start=0
    tmp=[]
    while start<number:
        string_entery=input("enter the elments")
        start+=1
        tmp.append(string_entery)
    return tmp
def elements(string_entery):
    return string_entery
def test(tmp):

    return [*map(len,tmp)] 


def main():
    original_string=entry()
    print("original strings")
    n=elements(original_string)
    print(elements(original_string))
    print("Lengths of the each element in a list non-empty string")
    print(test(n))
main()