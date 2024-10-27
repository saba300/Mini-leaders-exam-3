def century(year):
    if year/100==int(year/100):
        return int(year/100)
    else:
        return int(year/100)+1
    

print(century(1705))