f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day 1 Numbers.txt", "r")
content = f.read()
numbers = content.split()
for i in range(len(numbers)):
    iterator = i + 1
    firstNum = numbers[i]
    for j in range(iterator, len(numbers)):
        secondNum = numbers[j]
        # numSum = int(firstNum) + int(secondNum)
        for k in range(iterator + 1, len(numbers)):
            thirdNum = numbers[k]
            numSum = int(firstNum) + int(secondNum) + int(thirdNum)
            if numSum == 2020:
                print(firstNum, secondNum, thirdNum)
                print(int(firstNum) * int(secondNum) * int(thirdNum))
                break
        else:
            continue
        break
        
                
        


