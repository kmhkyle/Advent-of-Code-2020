f = open(r"C:\Users\Kyle\Documents\Advent of Code 2020\Day_10_Puzzle_Input.txt", "r")
content = f.read().split('\n')
content = [int(line) for line in content]
content.sort()
ones = 1
threes = 1
for i in range(len(content) - 1):
    if content[i + 1] - content [i] == 1:
        ones += 1
    elif content[i + 1] - content [i] == 3:
        threes += 1
print(ones * threes)

memo = {}
def countways(adapters, start, goal):
    k = (len(adapters), start)
    if k in memo:
        return memo[k]
    ways = 0
    if goal - start <= 3:
        ways += 1
    if not adapters:
        return ways
    if adapters[0] - start <= 3:
        ways += countways(adapters[1:], adapters[0], goal)
    ways += countways(adapters[1:], start, goal)
    memo[k] = ways
    return ways

print(countways(sorted(content), 0, max(content) + 3))
