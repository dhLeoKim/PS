import sys
sys.stdin = open("input_2178.txt")
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    lst[0][0] = -1

    while queue:
        i, j, cnt = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                lst[ni][nj] = cnt+1
                queue.append((ni, nj, cnt+1))


N, M = map(int, input().split())
lst = [list(map(int, list(input().strip()))) for _ in range(N)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

bfs()

print(lst[N-1][M-1])