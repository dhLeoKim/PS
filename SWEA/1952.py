import sys
sys.stdin = open('sample_input.txt')

def dfs(i):
    if i >= 13:
        ret.append(sum(arr))
        # print(arr)
        return

    # for i in range(k, 13):
    if lst[i]:
        arr.append(lst[i]*d1)
        dfs(i+1)
        arr.pop()
        arr.append(m1)
        dfs(i+1)
        arr.pop()
        arr.append(m3)
        dfs(i+3)
        arr.pop()
    else:
        dfs(i+1)


T = int(input())
for case in range(1, T+1):
    d1, m1, m3, y1 = map(int, input().split())
    lst = list(map(int, input().split()))

    lst = [0] + lst

    ret = []
    arr = []
    dfs(1)

    ret.append(y1)

    print(f'#{case} {min(ret)}')