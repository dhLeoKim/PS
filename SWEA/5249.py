import sys
sys.stdin = open('sample_input.txt')

from heapq import heappush, heappop

def prim(u):
    h = []
    ret = 0
    MST[u] = 1
    for nxt in graph[u]:
        heappush(h, nxt)

    cnt = 0
    while cnt < V:
        w, v = heappop(h)
        if MST[v]:
            continue
        ret += w
        MST[v] = 1
        cnt += 1
        for nxt in graph[v]:
            if not MST[nxt[1]]:
                heappush(h, nxt)

    return ret

T = int(input())
for case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    MST = [0]*(V+1)

    print(f'#{case}', prim(0))