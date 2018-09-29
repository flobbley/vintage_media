cassette = [' ______________ ','|   __    __   |','|  /  \  /  \  |','|  \__/  \__/  |','|  __________  |','|_/_O______O_\_|']
VHS = [' ______________________  ','|                      | ','|     ____________     | ','|    /  |      |  \    | ','|   |   |      |   |   | ','|    \__|______|__/    | ','||____________________|| ','|______________________| ']
floppy = [' _____________   ','||   |    _ |  | ','||   |   | ||  | ','||   |   |_||  | ','||___|______|  | ','| ___________  | ','||           | | ','||           | | ','||           | | ','||___________|_| ']
snes = ['    _____________     ',' __||           ||__  ','|__||           ||__| ','|__||___________||__| ','|__| ___________ |__| ','|__||           ||__| ','|__||___________||__| ']
def printSquare(side, obj, length):
    for n in range(side):
        for part in obj: 
            print(part * side)
    return ""

class triangle:
    
    def __init__(self,side,obj,length):
        self.side = side
        self.obj = obj
        self.length = length
    def upperleft(side, obj, length):
        row = side
        for n in range(side): 
            for part in obj: 
                print(part * row)
            row-=1
        return ""

    def upperright(side, obj, length):
        row = int(side)
        for a in range(0,row):
            for part in obj:
                parts = row - a
                space = ' '*length
                print(space * a,end="")
                print(part * parts)
        return ""
    
    def bottomright(side, obj, length):
        row = int(side)
        for a in range(row,0,-1):
            for part in obj:
                parts = row+1 - a
                space = ' '*length
                print(space * int(a-1),end="")
                print(part * parts)
        return ""

    def bottomleft(side, obj, length):
        row = side
        for n in range(0,side):
            for part in obj:
                print(part*int(n+1))
        return ""


def printCassettes():
    more = True
    while more:
        objects = [cassette, VHS, floppy, snes]
        obj = objects[int(input('What are you looking for?\n1. Cassettes\n2. VHS Tapes\n3. floppy disks\n4. SNES Cartridges\n'))-1]
        square = False
        length = len(obj[1])
        while not square:
            size = int(input("how many do you want?\n"))
            sizes = [1,2**2,3**2,4**2,5**2,6**2,7**2]
            if size in sizes:
                    square = True
            else:
                print('That\'s not square!')
        side = int(size**0.5)
        print('What shape?')
        print('1. Rectangle')
        print('2. Triangle')
        condition = int(input())-1
        if condition != 0:
            print('Where do you want them?')
            print('1. Upper Right')
            print('2. Upper Left')
            print('3. Bottom Right')
            print('4. Bottom left')
            condition = int(input())
        if condition == 0:
            print(printSquare(side, obj, length))
        elif condition == 1:
            print(triangle.upperright(side, obj, length))
        elif condition == 2:
            print(triangle.upperleft(side, obj, length))
        elif condition == 3:
            print(triangle.bottomright(side, obj, length))
        elif condition == 4:
            print(triangle.bottomleft(side, obj, length))
        if condition != 0:
            print('Yeah I know I didn\'t give you all of them, that\'s what you get for asking for a triangle')
        print('Want more?\n 1. Yes\n 2. No')
        wantMore = int(input())
        if wantMore == 2:
            break
    return ""

print(printCassettes())      
