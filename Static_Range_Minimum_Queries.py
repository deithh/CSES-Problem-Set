import math
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
    n = int(data[0].split()[0])
    seq = [int(x) for x in data[1].split()]

    tree, h = construct_tree(seq)
    for line in data[2:]:
        a, b = [int(x) - 1 for x in line.split()]
        print(seek_tree(tree, h, a, b))


main()