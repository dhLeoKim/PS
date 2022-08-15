def elecBus(K, N, lst):
    p = 0
    cnt = 0

    while True:
        if p + K >= N: return cnt
        p_next = 0
        for i in lst:
            if p < i <= p + K:
                p_next = i
        if p_next == 0 : return 0
        p = p_next
        cnt += 1

T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    print(f'#{i+1} {elecBus(K, N, lst)}')