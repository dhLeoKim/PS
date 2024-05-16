def solution(s):
    string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num, string in enumerate(string):
        s = s.replace(string, str(num))

    return int(s)

s = "one4seveneight"

print(solution(s))