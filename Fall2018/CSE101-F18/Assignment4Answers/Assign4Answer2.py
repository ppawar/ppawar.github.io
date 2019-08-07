from random import shuffle


def compare(a, b):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    order = ['J', 'Q', 'K', 'A']
    if a[-1] < b[-1]:
        return True
    if a[-1] > b[-1]:
        return False
    if a[-2] not in alphabet and b[-2] in alphabet:
        return True
    if a[-2] in alphabet and b[-2] not in alphabet:
        return False
    if a[-2] not in alphabet and b[-2] not in alphabet:
        return int(a[:-1]) < int(b[:-1])
    return order.index(a[0]) < order.index(b[0])


def merge(u, v):
    res = []
    i = 0
    j = 0
    while True:
        if (i < len(u)) and (j < len(v)):
            if compare(u[i], v[j]):
                res.append(u[i])
                i = i + 1
            else:
                res.append(v[j])
                j = j + 1
        elif (i < len(u)) and (j >= len(v)):
            res = res + u[i: len(u)]
            return res
        elif (i >= len(u)) and (j < len(v)):
            res = res + v[j: len(v)]
            return res
        else:  # (i >= len(u)) and (j >= len(v))
            print('cannot be here')
            return None


def merge_groups(a, group_size):
    for i in range(0, len(a), 2 * group_size):
        j = i + group_size
        k = j + group_size
        a[i:k] = merge(a[i:j], a[j:k])


def msort(a):
    size = 1
    while size < len(a):
        merge_groups(a, size)
        size = size * 2


def main():
    orderedDeck = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", "2D", "3D",
                   "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", "2H", "3H", "4H", "5H", "6H", "7H",
                   "8H", "9H", "10H", "JH", "QH", "KH", "AH", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS",
                   "KS", "AS"]
    shuffle(orderedDeck)
    msort(orderedDeck)
    print(orderedDeck)


main()
