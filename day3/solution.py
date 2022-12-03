file_content = ""
with open("input.txt") as f:
    file_content = f.read()

from string import ascii_letters as letters
rucksacks = file_content.split('\n')
priority = lambda x : letters.index(x) + 1

# Part 1
total = 0
for sack in rucksacks:
    first_half = sack[0:len(sack)//2]
    second_half = sack[len(sack)//2:len(sack)]
    common_items = set(first_half).intersection(second_half)
    total += sum([priority(x) for x in common_items])
print(total)

# Part 2
total = 0
for i in range(0, len(rucksacks), 3):
    common_items = set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2])
    total += sum([priority(x) for x in common_items])
print(total)