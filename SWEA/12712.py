import sys
sys.stdin = open('in1.txt')

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di1 = [1, 0, -1, 0]
    dj1 = [0, 1, 0, -1]

    di2 = [1, 1, -1, -1]
    dj2 = [1, -1, -1, 1]

    max_val = 0
    for i in range(N):
        for j in range(N):
            temp1 = lst[i][j]
            temp2 = lst[i][j]
            for k in range(4):
                for w in range(1, M):
                    ni1, nj1 = i + di1[k]*w, j + dj1[k]*w
                    if 0 <= ni1 < N and 0 <= nj1 < N:
                        temp1 += lst[ni1][nj1]

                    ni2, nj2 = i + di2[k]*w, j + dj2[k]*w
                    if 0 <= ni2 < N and 0 <= nj2 < N:
                        temp2 += lst[ni2][nj2]

            max_val = max(temp1, temp2, max_val)

    print(f'#{case+1} {max_val}')