def checkView(N, lst):
    ret = 0
    i = 2
    # index의 앞2 뒤2 idx중, max(lst[idx])와 lst[i]의 차이만큼 저장
    # ret += lst[i] - max{lst[i-2, i-1, i+1, i+2]}
    # if lst[i] < max{lst[i-2, i-1, i+1, i+2]} 이면 continue
    while i < N - 2:
        temp = [lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2]]
        max_temp = 0
        for j in temp:
            if j > max_temp: max_temp = j
        if lst[i] <= max_temp:
            i += 1
            continue
        else:
            ret += lst[i] - max_temp
            i += 3

    return ret

T = 10

for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{i + 1} {checkView(N, lst)}')