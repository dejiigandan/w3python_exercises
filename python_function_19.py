def test(arg1):
    def adder(arg2):
        nonlocal arg1
        arg1 += 1
        return arg1 + arg2
    return adder()


result = test(4)
print(result(4))