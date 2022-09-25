import sys
sys.stdin = open('sample_input.txt')

def dfs(i, j):
    if len(arr) == 7:
        temp = ''.join(arr)
        if temp not in ret:
            ret.append(temp)
        return

    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            arr.append(str(lst[ni][nj]))
            dfs(ni, nj)
            arr.pop()

T = int(input())
for case in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(4)]

    ret = []
    for i in range(4):
        for j in range(4):
            arr = [str(lst[i][j])]
            dfs(i, j)

    print(f'#{case} {len(ret)}')