import sys
sys.stdin = open('input1767.txt')

def dfs(idx, c, l):
    global ret
    if idx == M:
        if c > ret[0]:
            ret = [c, l]
        elif c == ret[0] and l < ret[1]:
            ret = [c, l]
        return
    si, sj = start[idx]
    for k in range(4):
        
                # connect
        i, j = si, sj
        temp = 0
        while True:
            ni, nj = i+di[k], j+dj[k]
            if ni == -1 or ni == N or nj == -1 or nj == N: 
                l += temp
                c += 1
                break
            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == 0:
                    lst[ni][nj] = 2
                    temp += 1
                else:
                    break
            i, j = ni, nj

        dfs(idx+1, c, l)    # dfs 완전탐색

        # disconnect
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            l -= temp
            c -=1
        if lst[i][j] == 1:
            continue
        while True:
            lst[i][j] = 0
            ni, nj = i-di[k], j-dj[k]
            if ni == si and nj == sj: 
                break
            i, j = ni, nj

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    start = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if lst[i][j]:
                start.append((i, j))

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    M = len(start)
    ret = [0, 144]
    dfs(0, 0, 0)

    print(f'#{tc}', ret[1])