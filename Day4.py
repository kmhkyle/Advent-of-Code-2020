f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day4PuzzleInput.txt", "r")
content = f.read().split('\n\n')
passportList = []
for line in content:
    passportList.append(line.replace('\n',' '))

count = 0
passportFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for line in passportList:
    passport = {}
    validPassport = 'True'
    fields = line.split()
    for field in fields:
        key, value = field.split(':')
        passport[key] = value
    for key in passportFields:
        if key not in passport:
            validPassport = False
            break
        # Comment out rest of for loop for part 1
        validPassportField = False
        if key == 'byr':
            validPassportField = 1920 <= int(passport['byr']) <= 2002
        elif key == 'iyr':
            validPassportField = 2010 <= int(passport['iyr']) <= 2020
        elif key == 'eyr':
            validPassportField = 2020 <= int(passport['eyr']) <= 2030
        elif key == 'hgt':
            if passport['hgt'].endswith('cm'):
                validPassportField = 150 <= int(passport['hgt'][:-2]) <= 193
            elif passport['hgt'].endswith('in'):
                validPassportField = 59 <= int(passport['hgt'][:-2]) <= 76
        elif key == 'hcl':
            validPassportField = (passport['hcl'][0] == '#' and len(passport['hcl']) == 7)
            if validPassportField:
                for letter in passport['hcl'][1:]:
                    validPassportField = letter in '0123456789abcdef'
        elif key == 'ecl' :
            validPassportField = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            validPassportField = len(passport['pid']) == 9 and passport['pid'].isdigit()
        
        validPassport = validPassport and validPassportField
    
    if validPassport:
        count += 1

 
print(count)