# 2차원 배열 탐색 연습
# for문 한번에 작은 9칸도 검사할 수 있을까?

T = int(input())
for case in range(T):
    lst = [list(map(int, input().split())) for _ in range(9)]
    ret = 1

    # row, col 방향 count하는 배열 0으로 초기화, idx=0은 1로 초기화
    for i in range(9):
        temp_row = [0]*10
        temp_col = [0]*10
        temp_row[0] = temp_col[0] = 1
        # row, col 방향을 탐색하며 count 배열 채우기
        for j in range(9):
            temp_row[lst[i][j]] += 1
            temp_col[lst[j][i]] += 1
        # 0이 남아있으면 다 채워지지 않았으므로 스도쿠 실패
        if 0 in temp_row or 0 in temp_col:
            ret = 0
            break

    # 작은 9칸 검사, 델타 활용하여 9칸 탐색
    di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 0, 1, -1, 0 ,1]
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            temp_cube = [0] * 10
            temp_cube[0] = 1
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                temp_cube[lst[ni][nj]] += 1
            if 0 in temp_cube:
                ret = 0
                break

    print(f'#{case+1} {ret}')