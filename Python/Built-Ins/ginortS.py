
lower, upper, odd, even = "","","",""
s = sorted(input())
for e in s:
    if e.islower():
        lower += e
    elif e.isupper():
        upper += e
    elif int(e) % 2 != 0:
        odd += e
    else:
        even += e
print(lower+upper+odd+even)
    