from collections import deque


n= int(input())

queue = deque(range(1, n+1))


while len(queue):

    queue.rotate(-1)
    print(queue.popleft(), end = ' ')

