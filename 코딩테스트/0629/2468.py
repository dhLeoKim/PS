import sys
sys.stdin = open('input_2468.txt')
input = sys.stdin.readline

from collections import deque

def bfs(si, sj, height):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = True
    
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and lst[ni][nj] > height:
                queue.append((ni, nj))
                visited[ni][nj] = True


N = int(input())
lst = []
max_val = 0
for _ in range(N):
    row = list(map(int, input().split()))
    lst.append(row)
    max_val = max(max_val, max(row))

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

ret = [0]*(max_val+5)
for height in range(max_val):
    visited = [[False]*N for _ in range(N)]
    temp_ret = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lst[i][j] > height:
                bfs(i, j, height)
                temp_ret += 1
    
    ret[height] = temp_ret

print(max(ret))