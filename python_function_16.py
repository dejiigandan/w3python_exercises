
def square(arg1):
    mylist=[]
    for n in range(1, arg1 + 1):
        n = n**2
        mylist.append(n)
    print(mylist)
square(30)