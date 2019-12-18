

def sorter(arg1):
    b = arg1.split("-")
    b.sort()
    "-".join(b)
    return arg1

print(sorter(input("Your sequence: ")))
