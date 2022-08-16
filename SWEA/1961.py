# 2차원 배열 인덱스 접근 연습!!!
# 복작해지면 헷갈리지 않도록 적으면서 code작성하기!

T = int(input())
for case in range(T):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    ret = [[0]*3 for _ in range(N)]

    for i in range(N):
        temp90 = []
        temp180 = []
        temp270 = []
        # 뒤에서 앞으로 가는 idx 접근 연습하기
        for j in range(N):
            temp90.append(lst[N-1-j][i])
            temp180.append(lst[N-1-i][N-1-j])
            temp270.append(lst[j][N-1-i])
        ret[i][j-N+1] = ''.join(temp90)
        ret[i][(j-N+2)%N] = ''.join(temp180)
        ret[i][(j-N+3)%N] = ''.join(temp270)

    print(f'#{case+1}')
    for i in range(N):
        print(*ret[i])