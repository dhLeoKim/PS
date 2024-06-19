import sys
sys.stdin = open('input_2583.txt')
input = sys.stdin.readline

from collections import deque

def bfs(si, sj, cnt):
    queue = deque()
    queue.append((si, sj))
    lst[si][sj] = 1
    area = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 0:
                queue.append((ni, nj))
                lst[ni][nj] = cnt
                area += 1

    return area


M, N, K = map(int, input().split())
lst = [[0]*M for _ in range(N)]
for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            lst[i][j] = -1

ret_cnt = 0
ret_lst = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            ret_cnt += 1
            area = bfs(i, j, ret_cnt)
            ret_lst.append(area)

print(ret_cnt)
print(*sorted(ret_lst))