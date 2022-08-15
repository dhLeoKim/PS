def checkBabygin(lst):
    c = [0] * 12
    triplet = 0
    run = 0
    # 입력을 count하여 c배열에 저장
    for i in lst: c[i] += 1
    # check triplet
    for i in range(len(c)):
        if c[i] // 3 == 1:
            triplet += 1
            c[i] -= 3
        elif c[i] // 3 == 2: return 1
    # check run
    for i in range(len(c)):
        if c[i] ==2 and c[i+1] == 2 and c[i+2] == 2: return 1
        elif c[i] > 0 and c[i+1] > 0 and c[i+2] > 0:
            run += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
    # 모두 만족하면 1 반환
    return 1 if run + triplet == 2 else 0

N = int(input())

for i in range(N):
    lst = list(map(int, input()))
    print(f'#{i+1} {checkBabygin(lst)}')