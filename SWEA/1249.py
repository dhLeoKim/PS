import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

def dijkstra(start):
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    h = []
    i, j = start
    d[i][j] = 0
    heappush(h, (0, i, j))
    while h:
        dist, i, j = heappop(h)
        if dist > d[i][j]:
            continue
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                ndist = dist + lst[ni][nj]
                if ndist < d[ni][nj]:
                    d[ni][nj] = ndist
                    heappush(h, (ndist, ni, nj))

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, list(input()))) for _ in range(N)]

    INF = 1e9
    d = [[INF]*N for _ in range(N)]

    dijkstra((0, 0))

    print(f'#{case}', d[N-1][N-1])