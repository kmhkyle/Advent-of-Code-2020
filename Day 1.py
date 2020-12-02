f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day 1 Numbers.txt", "r")
content = f.read()
numbers = content.split()
for i in range(len(numbers)):
    iterator = i + 1
    firstNum = numbers[i]
    for j in range(iterator, len(numbers)):
        secondNum = numbers[j]
        numSum = int(firstNum) + int(secondNum)
        if numSum == 2020:
            print(firstNum, secondNum)
            print(int(firstNum) * int(secondNum))
            break
        


