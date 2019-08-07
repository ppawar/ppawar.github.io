from PythonLabs.RandomLab import RandomList


def scrabble_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if len(a[min]) > len(a[j]):
                min = j
            elif len(a[min]) == len(a[j]) and a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


def main():
    a = RandomList(20, 'words')
    print(scrabble_sort(a))


main()
