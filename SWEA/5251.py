import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop, heappush

def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    while h:
        dist, now = heappop(h)
        if d[now] < dist:
            continue
        print(now)
        for w, v in graph[now]:
            dist_nxt = dist + w
            if dist_nxt < d[v]:
                d[v] = dist_nxt
                heappush(h, (dist_nxt, v))
        # print(d)

T = int(input())
for case in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    INF = 1e9
    d = [INF]*(N+1)

    dijkstra(0)

    print(d)
    print(f'#{case}', d[N])