def sc(apple):
    for x in range(len(apple)):
        for y in range(len(apple[x])):
            if apple[x][y] == 'B':
                return [x,y]
def sc(apple):
    return [[x,y.index("B")] for x,y in enumerate(apple) if "B" in y][0]
def sc(apple):
    for i in apple :
        for j in i:
            if j == "B" :
                return [apple.index(i),i.index(j)]