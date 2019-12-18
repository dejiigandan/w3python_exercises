import sys
import string
mystring = "The quick brown fox jumps over the lazy dog"


def ispanagram(arg1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(arg1.lower())


print(ispanagram(mystring))
