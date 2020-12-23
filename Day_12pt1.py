f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_12_Puzzle_Input.txt", "r")
content = f.read().split('\n')
northSouth = 0
eastWest = 0
currentDirection = 90
directions = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}


def moveDirection(direction, movement):
    global northSouth, eastWest
    if direction == 'N':
        northSouth += movement
    elif direction == 'S':
        northSouth -= movement
    elif direction == 'E':
        eastWest += movement
    elif direction == 'W':
        eastWest -= movement

for line in content:
    moveDirection(line[0], int(line[1:]))
    if line[0] == 'L':
        currentDirection = (currentDirection - int(line[1:])) % 360 
    elif line[0] == 'R':
        currentDirection = (currentDirection + int(line[1:])) % 360 
    elif line[0] == 'F':
        moveDirection(directions[currentDirection], int(line[1:]))
    
print(abs(northSouth) +  abs(eastWest))