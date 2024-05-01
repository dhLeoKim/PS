def solution(N, number):
    dp = []
    for _ in range(9):
        dp_set = set()
        dp.append(dp_set)

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))

        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0:
                        dp[i].add(x//y)
    
        if number in dp[i]:
            return i

    return -1

N = 5
number = 12

print(solution(N, number))