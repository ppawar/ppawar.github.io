from PythonLabs.RandomLab import RandomList


def solution(A):
    a = A[0]*A[1]*A[2]*A[3]
    b = A[0]*A[1]*A[-2]*A[-1]
    c = A[-4]*A[-3]*A[-2]*A[-1]
    return max(a, b, c)


def main():
    length = 15
    A = RandomList(length)
    for i in range(length//2):
        A[i] = -A[i]
    print(solution(sorted(A)))


main()
