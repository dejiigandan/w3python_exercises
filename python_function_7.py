mystring = "The quick Brow Fox"

uppercount = 0
lowercount = 0
for e in mystring:
    if e.isupper():
        uppercount = uppercount + 1
    elif e.islower():
        lowercount = lowercount + 1

print(uppercount)
print(lowercount)

