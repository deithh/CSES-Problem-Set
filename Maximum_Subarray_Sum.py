n = int(input())
arr  = [int(x) for x in input().split()]


max_sum = float("-inf")
before = float("-inf")
current = float("-inf")

for i in arr:
    current = max(before+i, i)
    if current > max_sum:
        max_sum = current
    before = current

print(max_sum)
