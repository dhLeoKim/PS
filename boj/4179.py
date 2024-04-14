import sys
sys.stdin = open('input_4179.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start, fire):
    queue = deque()
    queue.append((False, start[0], start[1], 1))
    lst[start[0]][start[1]] = 1
    visited[start[0]][start[1]] = '.'

    for fi, fj in fire:
        queue.append((True, fi, fj, 1))
        visited[fi][fj] = 'F'

    while queue:
        isFire, i, j, t = queue.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if isFire and visited[ni][nj] != '.':
                    visited[ni][nj] = 'F'
                    queue.append((True, ni, nj, t+1))
                elif not isFire and lst[ni][nj] == '.' and visited[ni][nj] != 'F':
                    lst[ni][nj] = t+1
                    queue.append((False, ni, nj, t+1))

                    if ni == 0 or ni == R-1 or nj == 0 or nj == C-1:
                        return t+1
                    
    return 'IMPOSSIBLE'


R, C = map(int, input().split())
lst = []
visited = []
fire = []
for i in range(R):
    row = list(input().strip())
    lst.append(row[:])
    visited.append(row[:])
    for j in range(C):
        if row[j] == 'J':
            start = [i, j]
        elif row[j] == 'F':
            fire.append((i, j))

di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]

ret = bfs(start, fire)

print(ret)