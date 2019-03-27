def rangedemo(lowernum, uppernum, interval):
    listnum = range(lowernum, uppernum, interval)
    return listnum


evenlist = rangedemo(0, 20, 2) #even numbers
for i in evenlist:
    print(i, end=" ")
oddlist = rangedemo(1, 20, 2)#odd numbers
print()
for i in oddlist:
    print(i, end=" ")
mult3list = rangedemo(0, 20, 3) #multiples of 3
print()
for i in mult3list:
    print(i, end=" ")
