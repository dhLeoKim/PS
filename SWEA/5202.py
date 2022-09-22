import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    lst.sort(key= lambda x: x[1])

    ret = [lst[0]]
    for i in lst:
        if i[0] >= ret[-1][1]:
            ret.append(i)

    print(f'#{case} {len(ret)}')