f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_7_Puzzle_Input.txt", "r")
content = f.read().split('\n')
hasShinyGoldBag = []
validBag = []
bagsLookingFor = ['shiny gold']
newBags = []
count = 0
while len(bagsLookingFor) > 0:
    newBags = []
    for i in content:
        bagsContained = []
        bags= ''
        line = i.split()
        primaryBag = "{} {}".format(line[0], line[1])
        if line[4] == 'no':
            pass
        else:
            for j in range(4, len(line)):
                if (j % 4) == 0:
                    pass
                elif (j % 4) == 3:
                    bagsContained.append(bags)
                    bags = ''
                elif (j % 4) == 1:
                    bags += line[j] + ' '
                elif (j % 4) == 2:
                    bags += line[j]
        for b in bagsLookingFor:
            if b in bagsContained:
                newBags.append(primaryBag)
    bagsLookingFor = []
    
    for bag in newBags:
        if bag not in hasShinyGoldBag:
            bagsLookingFor.append(bag)
            hasShinyGoldBag.append(bag)
        

print(len(hasShinyGoldBag))



