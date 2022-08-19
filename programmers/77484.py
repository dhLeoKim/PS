def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]            # 순위 저장
    
    corrects = 0
    for i in lottos:                        # 맞은 숫자 개수
        if i in win_nums: corrects += 1
    zeros = lottos.count(0)                 # 0 개수

    max_idx = corrects + zeros              # 최고
    min_idx = corrects                      # 최저
    answer = [rank[max_idx], rank[min_idx]]

    return answer

lottos = [45, 0, 0, 0, 0, 0]
win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))