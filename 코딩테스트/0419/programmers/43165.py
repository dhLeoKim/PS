ret = 0

def dfs(k, t, M, numbers, target):
    global ret

    if k == M:
        if t == target:
            ret += 1
        return

    dfs(k+1, t+numbers[k], M, numbers, target)
    dfs(k+1, t-numbers[k], M, numbers, target)

def solution(numbers, target):
    M = len(numbers)
    
    dfs(0, 0, M, numbers, target)

    return ret

numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))