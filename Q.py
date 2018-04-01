def f1(n):
    res = n // 4
    return res


def f2(a, b):
    cnt = 0
    for i in range(a, b + 1):
        L = []
        K = []
        while i != 0:
            x = i % 10
            K.append(x)
            if x not in L:
                L.append(x)
            i = i // 10

        if len(L) == len(K):
            cnt += 1
    return cnt


def f3(n, x):
    x.sort()
    a = 0
    b = 0
    while x != []:
        if a <= b:
            a = a + x[-1]
            x.pop()
        else:
            b = b + x[-1]
            x.pop()

    return (min(a, b), max(a, b))


if __name__ == '__main__':
    print(f1(8))
    a = 100
    b = 199
    print(f2(a, b))
    n = 5
    x = [10, 9, 7, 8, 3]
    print(f3(n, x))
