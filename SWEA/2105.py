import sys
sys.stdin = open('sample_input.txt')


#######################
# 1.

# def dfs(d, i, j):
#     if d == 4:
#         ret.append(len(arr))
#         # print(arr)
#         return
#
#     for d in range(d, d+2):
#         if d == 4:
#             return
#         if len(arr) == 1 and d == 1:
#             return
#         ni, nj = i + di[d], j + dj[d]
#         if 0 <= ni < N and 0 <= nj < N:
#             if d == 3 and lst[ni][nj] == arr[0]:
#                 dfs(d+1, i, j)
#             elif lst[ni][nj] not in arr:
#                 arr.append(lst[ni][nj])
#                 dfs(d, ni, nj)
#                 arr.pop()

def dfs(d, i, j):
    # if d == 4 and (i, j) == start:
    #     ret.append(len(arr))
    #     return

    for k in range(d, d+2):
        if k == 4 or (i, j) == start and k == 1:
            return
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if lst[ni][nj] not in arr:
                arr.append(lst[ni][nj])
                dfs(k, ni, nj)
                arr.pop()
            elif (ni, nj) == start:
                ret.append(len(arr))
                return
                # dfs(k+1, ni, nj)


T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di, dj = [1, 1, -1, -1], [1, -1, -1, 1]

    ret = []
    for i in range(N-2):
        for j in range(1, N-1):
            start = (i, j)
            arr = [lst[i][j]]
            dfs(0, i, j)

    print(f'#{case} {max(ret) if ret else -1}')