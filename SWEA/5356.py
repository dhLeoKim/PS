T = int(input())
for case in range(T):
    lst = []
    # 문제에 영향이 없는 char '^'을 공란표기 용으로 채우기
    for _ in range(5):
        temp = input()
        if len(temp) < 15: temp += '^'*(15-len(temp))
        lst.append(temp)

    # zip으로 전치 시킨뒤, ^ 제거하여 .join으로 출력
    ret = [''.join(list(x)) for x in zip(*lst)]
    ret = ''.join(ret)
    cnt = ret.count('^')
    ret = ret.replace('^', '', cnt)

    print(f'#{case+1} {ret}')