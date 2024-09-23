n = int(input())
nl = map(int, input().split())
srt = [0]*(n+1)
 
 
for i in nl:
	srt[i] = 1
 
 
for ind, i in enumerate(srt):
    if ind == 0:
        continue
    if i == 0:
        print(ind)
        break