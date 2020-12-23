f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_12_Puzzle_Input.txt", "r")
content = f.read().split('\n')
waypointNS = 1
waypointEW = 10
northSouth = 0
eastWest = 0

for line in content:
    movement = line[:1]
    amountMoved = int(line[1:])
    if movement == 'L':
        while amountMoved:
            waypointNS, waypointEW = waypointEW, -waypointNS
            amountMoved -= 90
    elif movement == 'R':
        while amountMoved:
            waypointNS, waypointEW = -waypointEW, waypointNS
            amountMoved -= 90
    elif movement == 'F':
        eastWest += waypointEW * amountMoved
        northSouth += waypointNS * amountMoved
    elif movement == 'N':
        waypointNS += amountMoved
    elif movement == 'E':
        waypointEW += amountMoved
    elif movement == 'S':
        waypointNS -= amountMoved
    elif movement == 'W':
        waypointEW -= amountMoved
        
print(abs(northSouth) + abs(eastWest))