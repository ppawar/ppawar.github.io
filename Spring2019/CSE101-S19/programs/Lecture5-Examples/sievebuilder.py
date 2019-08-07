from math import *

def sift(k, worksheet):
    for i in range(2*k, len(worksheet), k):
        worksheet[i] = None
    return worksheet

def removeNone(worksheet):
    listnum = []
    for i in range(len(worksheet)):
        if worksheet[i] != None:
            listnum.append(worksheet[i])
    return listnum

def sieve(worksheet1):
    for i in range(2, ceil(sqrt(len(worksheet1)))):
        worksheet1 = sift(i, worksheet1)
        worksheet1 = removeNone(worksheet1)
        for i in worksheet1:
            print(i, end=" ")

worksheet1 = [None, None] + list(range(2, 400))
sieve(worksheet1)
