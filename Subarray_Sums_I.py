_, E = [int(x) for x in input().split()]
seq = [int(x) for x in input().split()]



l, h = 0, 0
curr_sum = 0
res = 0


while h<len(seq):

    curr_sum += seq[h]

    while curr_sum > E and h>=l:
        curr_sum -= seq[l]
        l+=1

    if curr_sum == E:
        res += 1

    h+=1

print(res)
    

