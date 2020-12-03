f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day 2 Puzzle Input.txt", "r")
# data = []
# for line in f:
#     data.append(line.strip('\n'))


content = f.read()
data = content.split()
iterator = 1
amountLetters = []
key = []
letters = []
count = 0

for info in data:
    if iterator == 1:
        amountLetters.append(info)
        iterator += 1
    elif iterator == 2:
        key.append(info.strip(':'))
        iterator += 1
    else:
        letters.append(info)
        iterator = 1


for num in range(len(key)):
    letterCount = 0
    for listNum in range(len(amountLetters[num])):
        if amountLetters[num][listNum] == '-':
            hyphenNum = listNum
    firstNum = amountLetters[num][0:hyphenNum]
    secondNum = amountLetters[num][hyphenNum + 1:]
    if letters[num][int(firstNum) - 1] == key[num]:
        if letters[num][int(secondNum) - 1] != key[num]:
            count += 1
    elif letters[num][int(secondNum) - 1] == key[num]:
        count +=1


    ### For Part 1###
    # for letter in letters[num]:
    #     if letter == key[num]:
    #         letterCount += 1
    # if letterCount >= int(firstNum) and letterCount <= int(secondNum):
    #     count += 1

print(count)
            




