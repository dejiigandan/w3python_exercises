

def palid(myarg):

    b = myarg[::-1]
    print(b)
    return myarg == b

print(palid(input("Enter string here: ").replace(" ", "")))