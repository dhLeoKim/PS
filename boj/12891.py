import sys
sys.stdin = open('input_12891.txt')
input = sys.stdin.readline

S, P = map(int, input().split())
lst = list(input().strip())
A, C, G, T = list(map(int, input().split()))
chk_dict = {'A': A, 'C': C, 'G': G, 'T': T}

now_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
l = 0
r = P
ret = 0
chk_num = 0

chk_lst = lst[:r]
for char in chk_lst:
    now_dict[char] += 1
    
for key in chk_dict.keys():
    if now_dict[key] >= chk_dict[key]:
        chk_num += 1

if chk_num == 4:
    ret += 1

while r < S:
    now_dict[lst[r]] += 1
    if now_dict[lst[r]] == chk_dict[lst[r]] :
        chk_num += 1

    if now_dict[lst[l]] == chk_dict[lst[l]] :
        chk_num -= 1
    now_dict[lst[l]] -= 1

    if chk_num == 4:
        ret += 1    

    l += 1
    r += 1

print(ret)