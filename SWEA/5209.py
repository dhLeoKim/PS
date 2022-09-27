import sys
sys.stdin = open('sample_input.txt')

def backtracking(k, s):
    global ret
    if k == N:                  # 경우의 수 완성, 최소 저장
        if s < ret:
            ret = s
        return

    elif s >= ret:              # purnning
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(k+1, s+lst[k][i])
            visited[i] = False

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ret = 99*N
    visited = [False]*N
    backtracking(0, 0)

    print(f'#{case}', ret)