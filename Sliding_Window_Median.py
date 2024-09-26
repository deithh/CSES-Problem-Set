def solve(seq, k):
    kelner = []
    for i in range(k):
        insert(kelner, seq[i])

    d, j = 0, k
    for _ in range(n-k):
        print(median_presorted(kelner), end = ' ')
        kelner.remove(seq[d])
        insert(kelner, seq[j])
        d, j = d+1, j+1
    print(median_presorted(kelner), end = ' ')

def insert(array: list, num: int):
    if len(array) == 0:
        array.append(num)
        return
    for i in range(len(array)):
        if array[i]>= num:
            array.insert(i, num)
            break
    else:
        array.append(num)

def median_presorted(kelner):
    if len(kelner)%2 == 1:
        return kelner[len(kelner)//2]
    else:
        return min(kelner[len(kelner)//2], kelner[len(kelner)//2-1])

n, k = [int(x) for x in input().split()]
seq = list(map(int, input().split()))

solve(seq, k)

#to slow remove index change needed