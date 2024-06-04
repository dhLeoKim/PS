def solution(absolutes, signs):
    ret = 0
    for i in range(len(absolutes)):
        if signs[i]: ret += absolutes[i]
        else: ret -= absolutes[i]

    return ret

absolutes = [4,7,12]
signs = [True,False,True]

print(solution(absolutes, signs))