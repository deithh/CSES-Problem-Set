n, m, k = [int(x) for x in input().split()]
desires = [int(x) for x in input().split()]
apartments = [int(x) for x in input().split()]

desires.sort()
apartments.sort()

count = 0
a = 0
d = 0

while a < len(apartments) and d < len(desires):

    if abs(desires[d] - apartments[a]) <= k:
        a+=1
        d+=1
        count +=1
    
    elif desires[d] < apartments[a]:
        d+=1
    else:
        a+=1


print(count)

        
