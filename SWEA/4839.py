# 이진 탐색 횟수 반환 함수
def binarySearch(P, t):
    lst = list(range(1, P+1))
    s = 1
    e = P
    cnt = 1
    while s <= e:
        m = (s+e)//2
        # 중앙값인 경우, 검색 성공
        if lst[m-1] == t:
            return cnt
        # 중앙값보다 큰 경우, 뒷구간 검색
        elif lst[m] > t:
            e = m
        # 중앙값보다 작은 경우, 앞구간 검색
        else:
            s = m
        cnt += 1

T = int(input())
for case in range(T):
    P, Pa, Pb = map(int, input().split())

    a = binarySearch(P, Pa)
    b = binarySearch(P, Pb)

    # a와 b의 크기 비교
    if a < b: result = 'A'
    elif a > b: result = 'B'
    else: result = 0

    print(f'#{case+1} {result}')