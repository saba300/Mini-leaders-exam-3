def quarter_of(month):
    if int(month%3)==0:
        return int(month/3)
    else:
        return int(month/3)+1
    pass

print(quarter_of(4))