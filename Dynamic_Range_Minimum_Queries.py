import math
import cProfile
import sys
def seek_tree(tree, h, a, b):
    if a>b:
        return 0
    
    pa, pb = (1<<h) + a, (1<<h)+b
    res = min(tree[pa], tree[pb])

    while (pa//2 != pb//2):

        if pa%2 == 0:
            res = min(res, tree[pa+1])
        if pb%2 == 1:
            res = min(res, tree[pb-1])
        
        pa //= 2
        pb //= 2

    return res

def set_tree(tree, h, pos, x):
    target = (1<<h) + pos

    tree[target] = x

    while target > 1:
        target //= 2
        tree[target] = min(tree[target * 2], tree[target * 2 + 1])

def update_tree(tree, h):
    for i in range((1 << h) - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])


def construct_tree(seq):
    h = math.ceil(math.log2(len(seq)))
    nodes = 1<<(1+h)

    tree = [0]*nodes

    for ind, i in enumerate(seq):
        target = (1<<h) + ind
        tree[target] = i

    update_tree(tree, h)

    return tree, h

def main():
    data = [line.rstrip() for line in sys.stdin.readlines()]
    seq = [int(x) for x in data[1].split()]
    tree, h = construct_tree(seq)
    for line in data[2:]:
        type, v1, v2 = [int(x) for x in line.split()]
        if type == 1:
            v1 -= 1
            set_tree(tree, h, v1, v2)
        if type == 2:
            v1-=1
            v2-=1
            print(seek_tree(tree, h, v1, v2))


main()  