# 경로를 count배열에 저장하여
# 경로가 겹치면 +1
# count배열의 최대값이 결과

T = int(input())
for case in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    c = [0]*401
    for i in lst:
        # 큰 수의 방에서 작은 수의 방으로 오는 경우 고려
        if i[0] > i[1]: i.reverse()
        # 시작방과 끝방의 홀수, 짝수 고려
        for j in range(i[0] + i[0]%2 - 1, i[1] + i[1]%2 + 1):
            c[j] += 1

    # max압수
    # ret = max(c)
    ret = 0
    for i in c:
        if i > ret: ret = i

    print(f'#{case+1} {ret}')