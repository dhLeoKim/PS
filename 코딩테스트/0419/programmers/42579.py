def solution(genres, plays):
    table = {}
    for i in range(len(genres)):
        if table.get(genres[i], 0):
            table[genres[i]][0].append((plays[i], i))
            table[genres[i]][1] += plays[i]
        else:
            table[genres[i]] = [[(plays[i], i)], plays[i]]
    
    table_val = list(table.values())
    table_val.sort(reverse=True, key= lambda x: x[1])

    ret = []
    for temp in table_val:
        music = temp[0]
        music.sort(reverse=True, key= lambda x: x[0])
        for i in range(len(music)):
            if i == 2:
                break
            ret.append(music[i][1])

    return ret

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))