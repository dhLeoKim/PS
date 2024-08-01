import sys
sys.stdin = open('input_2170.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

ret = 0
str = lst[0][0]
end = lst[0][1]
for i in lst:
    if i[0] <= end:
        if i[1] > end:
            end = i[1]
    else:
        ret += end - str
        str = i[0]
        end = i[1]

ret += end - str
print(ret)