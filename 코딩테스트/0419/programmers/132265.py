def solution(topping):

    result = 0
    chk1 = {}
    for num in topping:
        if num in chk1:
            chk1[num] += 1
        else:
            chk1[num] = 1

    chk2 = {}
    for num in topping:
        if num in chk2:
            chk2[num] += 1
        else:
            chk2[num] = 1

        chk1[num] -= 1
        if chk1[num] == 0:
            del chk1[num]

        if len(chk1) == len(chk2):
            result += 1
        elif len(chk1) < len(chk2):
            break

    return result

topping = [1, 2, 1, 3, 1, 4, 1, 2]

print(solution(topping))