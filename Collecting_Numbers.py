n = int(input())
 
seq = [int(x) for x in input().split()]
 
pos = [0]*(n+1)
rounds = 1
 
 
for ind, i in enumerate(seq):
    pos[i] = ind
 
for i in seq:
    if pos[i-1] > pos[i]:
        rounds +=1
 
 
print(rounds)