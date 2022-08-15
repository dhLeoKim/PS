T = 10
for case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_row = sum_col = [0]*100
    sum_diag = [0, 0]

    for i in arr:
        sum_col = [x+y for x, y in zip(sum_col, i)]

    for i in range(100):
        sum_diag[0] += arr[i][i]

    arr = [list(x) for x in zip(*arr)]

    for i in arr:
        sum_row = [x+y for x, y in zip(sum_row, i)]

    for i in range(100):
        sum_diag[1] += arr[i][i]

    sum_total = sum_col + sum_row + sum_diag

    max_sum = 0
    for i in sum_total:
        if i > max_sum: max_sum = i

    print(f'#{case+1} {max_sum}')

#########################
# 전치 행렬
arr = [list(x) for x in zip(*arr)]

# 열 탐색
for i in range(100):
    temp = 0
    for j in range(100):
        temp += arr[j][i]

# 좌하단방향 대각선
temp = 0
for i in range(100):
    for j in range(100):
        temp += arr[99-i][i]