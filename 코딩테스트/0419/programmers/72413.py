def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for u in range(1, n+1):
        graph[u][u] = 0

    for u, v, w in fares:
        graph[u][v] = w
        graph[v][u] = w

    for k in range(1, n+1):
        for u in range(1, n+1):
            for v in range(1, n+1):
                if graph[u][k] + graph[k][v] < graph[u][v]:
                    graph[u][v] = graph[u][k] + graph[k][v]

    ret = INF
    for i in range(1, n+1):
        temp = graph[s][i] + graph[i][a] + graph[i][b]
        if temp < ret:
            ret = temp

    return ret

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))