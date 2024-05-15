def solution(today, terms, privacies):
    yyyy, mm, dd = map(int, today.split('.'))

    terms_dict = {}
    for _ in terms:
        type, period = _.split(' ')
        terms_dict[type] = int(period)

    ret = []
    for i in range(len(privacies)):
        day, type = privacies[i].split(' ')
        y, m, d = map(int, day.split('.'))
        diff = (yyyy - y)*12*28 + (mm - m)*28 + (dd - d)        

        if diff/28 >= terms_dict[type]:
            ret.append(i+1)

    return ret

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))