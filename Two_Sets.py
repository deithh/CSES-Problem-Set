def split_set(n):
    total = ((n+1)/2 * n)
    if total % 2 != 0:
        return 'NO'
    
    s1_sum = 0
    s1, s2 = [], []

    while 1:
        if n<1:
            break
        if s1_sum + n <= total//2:
            s1.append(n)
            s1_sum += n
        else:
            s2.append(n)
        n-=1

    l1 = len(s1)
    l2 = len(s2)
    s1 = " ". join(map(str, s1))
    s2 = " ". join(map(str, s2))

    return '\n'.join(map(str, ['YES', l1, s1, l2, s2]))

n = int(input())
print(split_set(n))