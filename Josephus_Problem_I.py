from collections import deque

n = int(input())
holds_sword = True

queue = deque(range(1, n+1))


while len(queue):
    if holds_sword:
        queue.append(queue.popleft())
    else:
        print(queue.popleft(), end = ' ')
    holds_sword = not holds_sword


    

