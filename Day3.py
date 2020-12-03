f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day3PuzzleInput.txt", "r")
data = []
for line in f:
    data.append(line.strip('\n'))


def Trajectory(slopeColumn, slopeRow):
    columnNum = 0
    rowNum = 0
    count = 0
    while rowNum < len(data):
        line = data[rowNum] * 100
        if line[columnNum] == '#':
            count += 1
        rowNum += slopeRow
        columnNum += slopeColumn
    return count
        

print(Trajectory(1,1) * Trajectory(3,1) * Trajectory(5,1) * Trajectory(7,1) * Trajectory(1,2))