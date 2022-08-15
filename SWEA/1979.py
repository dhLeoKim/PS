T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    # 주어진 arr 에서 row, col 끝에 0으로 이루어진 배열 추가
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]
    arr.append([0]*N)
    result = 0
    # 연속한 1 3칸 있는지 탐색
    for i in range(len(arr)-1):
        cnt_row = cnt_col = 0
        for j in range(len(arr)-1):
            # row 방향 탐색
            if arr[i][j]*arr[i][j+1] == 1:
                cnt_row += 1
            else:
                if cnt_row == K - 1:
                    result += 1
                cnt_row = 0
            
            # col 방향 탐색
            if arr[j][i]*arr[j+1][i] == 1:
                cnt_col += 1
            else:
                if cnt_col == K - 1:
                    result += 1
                cnt_col = 0

    print(f'#{case+1} {result}')