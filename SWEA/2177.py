import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(i, j, d):
    queue = deque()
    queue.append((i, j, d))
    visited[i][j] = True
    while queue:
        i, j, d = queue.popleft()
        temp[d] += lst[i][j]        # bfs 깊이를 index로 집의 갯수를 저장
        if d == K:                  # 최대 운영 비용까지 bfs 탐색
            continue
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = d+1
                queue.append((ni, nj, d+1))

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 최대 수익 구하기
    h = 0
    for row in lst:
        h += sum(row)
    max_income = h * M

    # 최대 운영 비용 구하기
    K = 1
    p = [0]
    while True:
        price = K*K + (K-1)*(K-1)
        if price > max_income:
            K = K-1
            break
        else:
            K += 1
            p.append(price)

    ret = 0
    for i in range(N):
        for j in range(N):
            temp = [0]*(K+1)
            visited = [[False] * N for _ in range(N)]
            bfs(i, j, 1)

            for l in range(1, len(temp)):                   # temp값 누적
                temp[l] += temp[l-1]
            for l in range(1, len(temp)):
                if M*temp[l] >= p[l] and temp[l] > ret:     # 이익이 0이상인지 확인, 최대값 저장
                    ret = temp[l]
                    idx = (i, j)

    print(f'#{case}', ret)