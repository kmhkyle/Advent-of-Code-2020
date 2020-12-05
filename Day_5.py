f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_5_Puzzle_Input.txt", "r")
boardingPasses = f.read().split()
highestSeatID = 0
IDs = []
for boardingPass in boardingPasses:
    rowFloor = 0
    rowCeiling = 127
    columnFloor = 0
    columnCeiling = 7
    for letter in boardingPass:
        if letter == 'F':
            rowCeiling = int((rowCeiling - rowFloor) / 2) + rowFloor
        elif letter == 'B':
            rowFloor = int((rowCeiling - rowFloor) / 2) + 1 + rowFloor
        elif letter == 'L':
            columnCeiling = int((columnCeiling - columnFloor) / 2) + columnFloor
        elif letter == 'R':
            columnFloor = int((columnCeiling - columnFloor) / 2) + 1 + columnFloor
    row, column = rowFloor, columnFloor
    seatID = row * 8 + column
    IDs.append(seatID)
    if seatID > highestSeatID:
        highestSeatID = seatID
sortedIDs = sorted(IDs)
for index in range(len(sortedIDs) - 1):
    if sortedIDs[index + 1] - sortedIDs[index] != 1:
        myID = sortedIDs[index] + 1
print(myID)


