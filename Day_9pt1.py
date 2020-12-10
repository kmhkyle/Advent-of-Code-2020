f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_9_Puzzle_Input.txt", "r")
content = f.read().split('\n')
activeList = []
valid = False
index = 25
for i in range(25):
    activeList.append(content[i])
   
while True:
    for num in range(len(activeList) - 1):
        if valid:
            break
        firstNum = int(activeList[num])
        for num2 in range(num + 1, len(activeList)):
            secondNum = int(activeList[num2])
            answer = firstNum + secondNum
            if answer == int(content[index]):
                activeList.append(content[index])
                activeList.pop(0)
                valid = True
                index += 1
                break
    if valid:
        valid = False
        continue
    else:
        print(content[index])
        break

    
 