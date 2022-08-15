def check(lst):
    # column별 가장 높은 낙차를 찾아서 ret에 저장
    ret = [0 for _ in range(len(lst) + 1)]
    for i in range(len(lst)):
        if lst[i] != 0:
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]: ret[i] += 1
    # max 압수..
    # return max(ret)
    
    # max 낙차값 찾아서 반환
    max_ret = 0
    for i in ret:
        if i >= max_ret: max_ret = i

    return max_ret

T = int(input())

for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{i+1} {check(lst)}')
