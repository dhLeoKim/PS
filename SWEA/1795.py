import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

def dijkstra(start):
    h = []
    d[start][start] = 0
    heappush(h, (0, start))
    while h:
        dist, u = heappop(h)
        if d[start][u] < dist:
            continue
        for w, v in graph[u]:
            ndist = dist + w
            if ndist < d[start][v]:
                d[start][v] = ndist
                heappush(h, (ndist, v))

T = int(input())
for case in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    INF = 1e9
    d = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        d[i][0] = 0

    for i in range(1, N+1):
        dijkstra(i)

    ret = [0]*(N+1)
    for i in range(1, N+1):
        ret[i] = d[i][X] + d[X][i]

    print(f'#{case}', max(ret))