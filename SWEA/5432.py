T = int(input())
for case in range(T):
    lst = input()

    ret = 0
    cnt = 0
    for i in range(len(lst)):
        # ( 이면 막대기 +1
        if lst[i] == '(':
            cnt += 1
        # ) 이면 막대기 -1 인데,,,
        elif lst[i] == ')':
            cnt -= 1
            # 이전 항이 ( 였으면 레이저 이므로 ret에 추가
            if lst[i-1] == '(': ret += cnt
            # 이전 항이 ) 였으면 레이저로 잘리고 남은 끝부분 ret +1
            elif lst[i-1] == ')': ret += 1

    print(f'#{case+1} {ret}')
