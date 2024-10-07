n = int(input())
arrivals = [None] * n
leaves = [None] * n

for i in range(n):
    a, l = [int(x) for x in input().split()]
    arrivals[i] = a
    leaves[i] = l

arrivals.sort()
leaves.sort()

a = 0 
l = 0
count = 0
max_count = 0

while a<len(arrivals):
    if arrivals[a] < leaves[l]:
        count +=1
        if count > max_count:
            max_count = count
        a+=1
    elif arrivals[a] > leaves[l]: #times are distinct
        count -=1
        l+=1

print(max_count)


