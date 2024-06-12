import sys
input = sys.stdin.readline

from collections import deque

def BFS(i, j):
    cnt = 1
    queue = deque()
    queue.append((i, j))
    lst[i][j] = 0
    while queue:
        i, j = queue.popleft()
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and lst[ni][nj] == 1:
                cnt += 1
                lst[ni][nj] = 0
                queue.append((ni, nj))
    
    return cnt

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

ret = 0
max_cnt = 0
for i in range(n):
    cnt = 0
    for j in range(m):
        if lst[i][j] == 1:
            cnt = BFS(i, j)
            if cnt > max_cnt: max_cnt = cnt
            ret += 1

print(ret)
print(max_cnt)