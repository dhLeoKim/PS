import sys
sys.stdin = open('input_1182.txt')
input = sys.stdin.readline

def dfs(idx, total, length):
    global ret

    if idx == N:
        if total == S and length != 0:
            ret += 1
        return
    
    dfs(idx+1, total, length)
    dfs(idx+1, total + lst[idx], length+1)


N, S = map(int, input().split())
lst = list(map(int, input().split()))

ret = 0
dfs(0, 0, 0)

print(ret)