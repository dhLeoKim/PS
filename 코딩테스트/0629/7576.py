import sys
sys.stdin = open('input_7576.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    for i, j in start:
        queue.append((i, j, 1))

    while queue:
        i, j, cnt = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 0:
                lst[ni][nj] = cnt+1
                queue.append((ni, nj, cnt+1))


M, N = map(int, input().split())
start = []
lst = []
for i in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)
    for j in range(M):
        if lst[i][j] == 1:
            start.append([i, j])

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

bfs()

ret = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            ret = -1
            print(ret)
            exit()

    ret = max(ret, max(lst[i]))
    
print(ret-1)