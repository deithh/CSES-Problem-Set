n = int(input())
arr  = [int(x) for x in input().split()]

max_lenght = 0
lenght = 0
s = set()
p1, p2 = 0, 0 

while p1<len(arr):
    if arr[p1] not in s:
        s.add(arr[p1])
        lenght += 1
        if lenght > max_lenght:
            max_lenght = lenght
        p1+=1

    else:
        s.remove(arr[p2])
        lenght -=1
        p2+=1

print(max_lenght)
