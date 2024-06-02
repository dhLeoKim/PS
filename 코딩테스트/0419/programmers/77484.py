def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    corrects = 0
    for i in lottos:
        if i in win_nums: corrects += 1
    zeros = lottos.count(0)

    max_idx = corrects + zeros
    min_idx = corrects
    answer = [rank[max_idx], rank[min_idx]]

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))