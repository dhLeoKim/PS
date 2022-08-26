# dfs로 풀이

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    lst = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N-1, -1, -1):                                                    # 시작점 찾기
        if 2 in lst[i]:
            now = [i, lst[i].index(2)]

    result = 0
    visited = [[False]*N for _ in range(N)]
    stack = [now]

    # dfs
    while stack:                                                                # dfs
        visited[now[0]][now[1]] = True
        delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        for k in range(4):                                                      # 가능한 다음 경로 탐색
            nxt = [now[0] + delta[k][0], now[1] + delta[k][1]]
            if nxt[0] < 0 or nxt[0] >= N or nxt[1] < 0 or nxt[1] >=N: continue  # idx 범위 확인
            if lst[nxt[0]][nxt[1]] == 3:                                        # 다음 점이 도착점 판단
                result = 1
                stack = []
                break
            if not visited[nxt[0]][nxt[1]] and lst[nxt[0]][nxt[1]] == 0:        # 가능한 다음 점으로 진행
                stack.append(now)
                now = nxt
                break
        else:                                                                   # 한쪽 진행 경로 끝나면 이전 분기점으로 되돌아가기
            now = stack.pop()

    print(f'#{case+1} {result}')