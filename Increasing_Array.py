n = input()
seq = list(map(int, input().split()))
 
 
last = seq[0]
count = 0
for i in seq[1:]:
    moves = max(last - i, 0)
    count += moves
    last = i + moves
 
print(count)