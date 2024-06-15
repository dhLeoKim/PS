import sys
sys.stdin = open('input_4179.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    si, sj = start
    queue = deque()
    queue.append((si, sj, 1))
    lst[si][sj] = 1
    for fi, fj in fire:
        queue.append((fi, fj, -1))

    while queue:
        i, j, cnt = queue.popleft()

        # 탈출과 불의 확산이 동시에 이루어지기에, 탈출위치로 불이 번지는지도 확인 필요! (lst[i][j] != 'F')
        if cnt != -1 and (i == 0 or i == R-1 or j == 0 or j == C-1) and lst[i][j] != 'F':
            return cnt

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if cnt == -1 and lst[ni][nj] != 'F' and lst[ni][nj] != '#':
                    queue.append((ni, nj, -1))
                    lst[ni][nj] = 'F'
                elif cnt != -1 and lst[ni][nj] == '.':
                    queue.append((ni, nj, cnt+1))
                    lst[ni][nj] = cnt+1

    return "IMPOSSIBLE"


R, C = map(int, input().split())
lst = []
fire = []
for i in range(R):
    temp = list(input().strip())
    lst.append(temp)
    for j in range(C):
        if lst[i][j] == 'J':
            start = (i, j)
        elif lst[i][j] == 'F':
            fire.append((i, j))

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

ret = bfs(start)

print(ret)