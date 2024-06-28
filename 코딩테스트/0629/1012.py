import sys
sys.stdin = open('input_1012.txt')
input = sys.stdin.readline

from collections import deque

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    lst[si][sj] = 0

    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                lst[ni][nj] = 0
                queue.append((ni, nj))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    lst = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        lst[i][j] = 1

    ret = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                bfs(i, j)
                ret += 1

    print(ret)