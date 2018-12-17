from PythonLabs.Tools import RandomList
from PythonLabs.IterationLab import isearch


def mean(A):
    return sum(A)/len(A)


def test_search(length, times):
    A = RandomList(length)
    result = []
    for i in range(times):
        result.append(isearch(A, A.random('success')))
    return mean(result)


def main():
    print(test_search(1000, 250))


main()
