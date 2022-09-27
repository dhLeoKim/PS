import sys
sys.stdin = open('input.txt')

def backtracking(i, s):
    global ret
    if i == N:                      # 최대 저장
        if s > ret:
            ret = s
        return

    elif s <= ret:                  # prunning
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            backtracking(i+1, s*lst[i][j]/100)
            visited[j] = False

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ret = 0
    visited = [0]*N
    backtracking(0, 1)

    print(f'#{case} {ret*100:.6f}') # f-string 활용하여 자리수 출력