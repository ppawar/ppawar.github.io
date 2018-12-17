from PythonLabs.RecursionLab import RandomList


def is_empty(S):
    return not S


def push(S, element):
    S.insert(0, element)


def pop(S):
    return S.pop(0)


def top(S):
    return S[0]


def sortedInsert(S, element):
    if is_empty(S) or element > top(S):
        push(S, element)
    else:
        tmp = pop(S)
        sortedInsert(S, element)
        push(S, tmp)


def sortStack(S):
    if not is_empty(S):
        tmp = pop(S)
        sortStack(S)
        sortedInsert(S, tmp)


def main():
    S = RandomList(20)
    sortStack(S)
    print(S)


main()
