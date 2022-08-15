T = int(input())

for case in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # index를 이동시킬 배열 (delta)
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    num = 1
    i = 0
    # step 통일을 위해서, j는 -1 부터 출발
    j = -1
    k = 0
    # snail 출력
    for step in range(2*N, 0, -1):
        # 진행 방향의 step 횟수, step//2로 step 횟수를 두 번씩 유지
        # ex) N = 4 라면, 4, 3, 3, 2, 2, 1, 1
        # 한 방향의 step이 모두 끝나면, 방향 전환
        for _ in range(step//2):
            # k%4로 방향 변경
            i += move[k%4][0]
            j += move[k%4][1]
            arr[i][j] = num
            num += 1
        k += 1

    print(f'#{case+1}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
