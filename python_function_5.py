
def factorial(myarg):
    if myarg == 0:
        return 1
    else:
        return myarg * factorial((myarg-1))



print(factorial(4))