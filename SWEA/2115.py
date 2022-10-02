import sys
sys.stdin = open('sample_input.txt')

def calc(temp):
    temp.sort(reverse=True)
    n = len(temp)
    print(temp)
    for i in range(n):
        a = 0
        b = []
        for j in range(i, n):
            a += temp[j]
            b.append(temp[j])
            if a > C:
                a -= temp[j]
                b.pop()
        # ret = [x**2 for x in a]
        print(a, b)
    exit()
    pass

def dfs(i, j):
    if i > N-1 or len(arr) == 2:
        ret.append(sum(arr))
        print(arr, sum(arr))
        return
    # if i == N-1 and j+M-1 == N-1:
    #     return
    if j+M-1 > N-1:
        dfs(i+1, 0)
    else:
        if not visited[i][j]:
            temp = []
            for k in range(M):
                visited[i][j+k] = True
                temp.append(lst[i][j+k])
            arr.append(calc(temp))
            dfs(i, j+1)
            for k in range(M):
                visited[i][j + k] = False
            arr.pop()
        dfs(i, j+1)


T = int(input())
for case in range(1, T+1):
    N, M, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # print(N, M, C)
    #
    # for i in lst:
    #     print(i)

    if case != 2:
        continue

    visited = [[False]*(N) for _ in range(N)]

    arr = []
    ret = []
    dfs(0, 0)
    # print(ret)

    print(f'#{case}', max(ret))