from heapq import heappush, heappop

def solution(book_time):

    lst = []
    for start, end in book_time:
        lst.append([int(start[:2])*60 + int(start[3:]), int(end[:2])*60 + int(end[3:])])
    lst.sort()
    
    room = [0]
    for i in range(len(lst)):
        if lst[i][0] >= room[0]:
            heappop(room)
            heappush(room, lst[i][1]+10)
        else:
            heappush(room, lst[i][1]+10)

    return len(room)

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(book_time))