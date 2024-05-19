def solution(numbers, hand):
    L = 10
    R = 12
    answer = ''
    for i in numbers:
        if i == 0: i = 11
        if i%3 == 1:
            answer += 'L'
            L = i
        elif i%3 == 0:
            answer += 'R'
            R = i
        else:
            d_L = sum([abs(x-y) for x, y in zip(list(divmod(L-1, 3)), divmod(i-1, 3))])
            d_R = sum([abs(x-y) for x, y in zip(list(divmod(R-1, 3)), divmod(i-1, 3))])

            if d_L < d_R:
                answer += 'L'
                L = i
            elif d_L > d_R:
                answer += 'R'
                R = i
            else:
                if hand == 'left':
                    answer += 'L'
                    L = i
                elif hand == 'right':
                    answer += 'R'
                    R = i

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
result = "LRLLLRLLRRL"

print(solution(numbers, hand, result))