from heapq import heappush, heappop

def dijkstra(start):
    h = []
    heappush(h, (0, start))
    d[start] = 0

    while h:
        dist_u, u = heappop(h)
        
        if d[u] < dist_u:
            continue

        for v, w in graph[u]:
            dist_v = dist_u + w
            if d[v] > dist_v:
                d[v] = dist_v
                heappush(h, (dist_v, v))


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 1e11
d = [INF]*(N+1)

dijkstra(0)