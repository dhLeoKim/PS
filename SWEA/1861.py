import sys
sys.stdin = open('input.txt')

def dfs(i, j):
    stack = [(i, j)]
    cnt = 0
    while stack:
        i, j = stack.pop()
        cnt += 1
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj]-lst[i][j] == 1:  # 다음칸과의 차이가 1인지 확인
                stack.append((ni, nj))

    return cnt                                  # 몇 칸 진행가능한지 반환

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_val = -1
    for i in range(N):
        for j in range(N):
            cnt = dfs(i, j)                     # dfs
            if cnt > max_val:                   # 최대값 찾기
                max_val = cnt
                ret = [lst[i][j]]
            elif cnt == max_val:                # 최대값 중 최소 찾기 위해 저장
                ret.append(lst[i][j])

    print(f'#{case} {min(ret)} {max_val}')