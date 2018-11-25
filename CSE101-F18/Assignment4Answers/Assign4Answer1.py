def graycode(n):
    if n == 1:
        return ['0', '1']
    ret = graycode(n-1)
    ret += reversed(ret)
    for i in range(len(ret)):
        if(i < len(ret)//2):
            ret[i] = '0'+ret[i]
        else:
            ret[i] = '1'+ret[i]
    return ret


def main():
    n = int(input())
    print(graycode(n))


main()
