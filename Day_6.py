f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_6_Puzzle_Input.txt", "r")
content = f.read().split('\n\n')
groupAnswers = []
answers = 'abcdefghijklmnopqrstuvwxyz'
count = 0
for line in content:
    groupAnswers.append(line.replace('\n',' '))

for group in groupAnswers:
    groupList = group.split()
    answerCheck =''
    for letter in groupList[0]:
        answerCheck += letter
    for i in range(1, len(groupList)):
        for letter in answerCheck:
            if letter not in groupList[i]:
                answerCheck = answerCheck.replace(letter, '')
    count += len(answerCheck)
    
print(count)
