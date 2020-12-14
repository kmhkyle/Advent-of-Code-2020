f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_11_Puzzle_Input.txt", "r")
content = f.read().split('\n')
numOccupied = 0
updatedChart = []
row = ''
rowLength = len(content[0]) - 1

while True:
    for line in range(len(content)):
        for seat in range(len(content[line])):
            numAdj = 0
            if content[line][seat] != '.':
                for c in [-1, 0, 1]:
                    for r in [-1, 0, 1]:
                        if c != 0 or r != 0:
                            i = 1
                            while 0 <= line + c * i <= (len(content) - 1) and 0 <= seat + r * i<= rowLength:
                                if content[line + c * i][seat + r * i] != '.':
                                    if content[line + c * i][seat + r * i] == '#':
                                        numAdj +=1
                                        break
                                    break
                                i += 1                                    
            if content[line][seat] == 'L':
                if numAdj == 0:
                    row += str('#')
                    numOccupied += 1
                    if seat == rowLength:
                        updatedChart.append(row)
                        row = ''
                else:
                    row += str('L')
                    if seat == rowLength:
                        updatedChart.append(row)
                        row = ''
            elif content[line][seat] == '#':
                if numAdj > 4:
                    row += str('L')
                    if seat == rowLength:
                        updatedChart.append(row)
                        row = ''
                else:
                    row += str('#')
                    numOccupied += 1
                    if seat == rowLength:
                        updatedChart.append(row)
                        row = ''
            else:
                row += '.'
                if seat == rowLength:
                    updatedChart.append(row)
                    row = ''
    if content == updatedChart:
        print(numOccupied)
        break
    else:
        content = updatedChart
        updatedChart = []
        numOccupied = 0
            