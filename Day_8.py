f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_8_Puzzle_Input.txt", "r")
content = f.read().split('\n')

actionDict = {} 
for i in range(len(content)):
    if content[i][0:3] == 'jmp':
        actionDict[i] = 'jmp'
    elif content[i][0:3] == 'nop':
        actionDict[i] = 'nop'

for k,v in actionDict.items():
    if content[k][0:3] == 'jmp':
        content[k] = 'nop' + content[k][3:len(content[k])]
    elif content[k][0:3] == 'nop':
        content[k] = 'jmp' + content[k][3:len(content[k])]
    accumulator = 0
    goneAlready = []
    index = 0
    
    while True:
        try:
            goneAlready.append(index)
            action = content[index][0:3]
            posNeg = content[index][4]
            movement = int(content[index][5:len(content[index])])
            if action == 'acc':
                if posNeg == '+':
                    accumulator += movement
                else:
                    accumulator -= movement
                index += 1
            elif action == 'jmp':
                if posNeg == '+':
                    index += movement 
                else:
                    index -= movement
            elif action == 'nop':
                index += 1
            if index in goneAlready:
                break
        except IndexError:
            print('The accumulator is', accumulator)
            break
    # turn back
    if content[k][0:3] == 'jmp':
        content[k] = 'nop' + content[k][3:len(content[k])]
    elif content[k][0:3] == 'nop':
        content[k] = 'jmp' + content[k][3:len(content[k])]
        
# print(actionDict)    
# print(accumulator)
# print(goneAlready)
