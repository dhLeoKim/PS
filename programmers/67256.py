def solution(numbers, hand):
    # phone = {}
    # phone[0] = [3, 2]
    # for i in range(1, 10):
    #     phone[i] = list(divmod(i, 3))

    # L = [3, 1]
    # R = [4, 0]
    # answer = ''
    # for i in numbers:
    #     d_L = sum([abs(x-y) for x, y in zip(L, phone[i])])
    #     d_R = sum([abs(x-y) for x, y in zip(R, phone[i])])
    #     print(d_L, d_R)
    #     if d_L < d_R: 
    #         answer += 'L'
    #         L = phone[i]
    #     elif d_L > d_R:
    #         answer += 'R'
    #         R = phone[i]
    #     else:
    #         if hand == 'left':
    #             answer += 'L'
    #             L = phone[i]
    #         elif hand == 'right':
    #             answer += 'R'
    #             R = phone[i]

    L = 10
    R = 12
    answer = ''
    for i in numbers:
        if i == 0: i = 11               # 좌표를 위해 0은 11로 취급
        if i%3 == 1:                    # 1 4 7
            answer += 'L'
            L = i
        elif i%3 == 0:                  # 3 6 9
            answer += 'R'
            R = i
        else:                           # 2 5 8 0
            # 좌표를 계산해서 거리를 비교
            d_L = sum([abs(x-y) for x, y in zip(list(divmod(L-1, 3)), divmod(i-1, 3))])
            d_R = sum([abs(x-y) for x, y in zip(list(divmod(R-1, 3)), divmod(i-1, 3))])

            if d_L < d_R:
                answer += 'L'
                L = i
            elif d_L > d_R:
                answer += 'R'
                R = i
            else:                       # 거리가 동일하면 hand 확인
                if hand == 'left':
                    answer += 'L'
                    L = i
                elif hand == 'right':
                    answer += 'R'
                    R = i

    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
# hand = "left"
print(solution(numbers, hand))