def solution(clothes):

    clothes_dict = {}
    for cloth in clothes:
        if clothes_dict.get(cloth[1], 0):
            clothes_dict[cloth[1]] += [cloth[0]]
        else:
            clothes_dict[cloth[1]] = [cloth[0]]
    
    # 옷을 입는 경우의 수는 (X+1)(Y+1)(Z+1)... 으로 구할 수 있다.
    # XYZ + XY + YZ + ZX + X + Y + X + 1
    # 이 때 최종 결과값에서 아무것도 입지않는 경우인 1을 빼야함
    ret = 1
    for key, value in clothes_dict.items():
        ret *= (len(value) + 1)
    
    return ret-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))