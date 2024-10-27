def number(bus_stops):
    cnt=0
    for i in bus_stops:
        cnt=cnt+i[0]
        cnt=cnt-i[1]
        
    return cnt


print(number([[10,0],[3,5],[5,8]]))