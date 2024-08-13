import sys
sys.stdin = open('input_6603.txt')
input = sys.stdin.readline

def dfs(idx, s):
    if idx == 6:
        print(*arr)
        return

    for i in range(s, len(lst)):
        if lst[i] not in arr:
            arr.append(lst[i])
            dfs(idx+1, i+1)
            arr.pop()


k = 1
while k:
    k, *lst = map(int, input().split())

    arr = []
    dfs(0, 0)

    print()