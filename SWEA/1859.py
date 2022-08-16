# 더 좋고 빠른 방법이 있을까?
# => max를 뒤에서부터 구하는 방법!!

# 구간 최대값 찾기
# 구간 최대값 전까지는 매입
# 최대값에서 모두 팔고
# 이후 다음 구간의 최대값 전까지 모두 매입
# 반복

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    ret = 0
    while len(lst):
        # max 압수
        # maxVal = max(lst)
        # maxIdx = lst.index(maxVal)

        # max값인 idx 찾기
        maxIdx = 0
        for i in range(len(lst)):
            if lst[i] > lst[maxIdx]: maxIdx = i

        # maxIdx전까지 모두 매입
        buy = 0
        for i in range(maxIdx):
            buy += lst[i]

        # maxIdx에서 모두 판매
        ret += lst[maxIdx]*maxIdx - buy

        # lst를 maxIdx 뒷 구간으로 update하고 반복
        lst = lst[maxIdx+1:]

    print(f'#{case+1} {ret}')