from bisect import bisect_left

def solution(info, query):

    def createKey(idx, key, i):
        if idx == 4:
            if applicant.get(key, 0):
                applicant[key].append(info[i][4])
            else:
                applicant[key] = [info[i][4]]

            return

        createKey(idx+1, key + info[i][idx], i)
        createKey(idx+1, key + '-', i)
    
    N = len(info)
    for i in range(N):
        info[i] = list(info[i].split())
        info[i][4] = int(info[i][4])

    info.sort(key=lambda x: x[4])

    applicant = {}
    for i in range(N):
        createKey(0, '', i)

    result = []
    for cond in query:
        A, B, C, DE = cond.split(' and ')
        D, E = DE.split(' ')
        key = A + B + C + D
        if applicant.get(key):
            val = applicant[key]
            result.append(len(val) - bisect_left(val, int(E)))
        else:
            result.append(0)

    return result

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))