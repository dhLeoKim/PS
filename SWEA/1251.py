import sys
sys.stdin = open('re_sample_input.txt')

from itertools import combinations

def find(x):
    while p[x] != x:
        x = p[x]
    return x

def kruskal():
    ret = 0
    for w, u, v in edge:
        if find(u) != find(v):
            p[find(v)] = find(u)
            ret += w

    return ret

T = int(input())
for case in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    lst = [[x, y] for x, y in zip(x_lst, y_lst)]


    edge = []
    for s, e in combinations(list(range(N)), 2):
        LL = (lst[s][0] - lst[e][0])**2 + (lst[s][1] - lst[e][1])**2
        w = E*LL
        edge.append((w, s, e))

    edge.sort()
    p = [i for i in range(N)]

    ret = kruskal()

    print(f'#{case} {ret:.0f}')