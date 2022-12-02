file_content = ""
with open("input.txt") as f:
    file_content = f.read()

elves = [x.split('\n') for x in file_content.split('\n\n')]
elves_total = sorted([sum([int(y) for y in x]) for x in elves], reverse=True)

print(f"Max: {elves_total[0]}")
print(f"Top 3 sum: {sum(elves_total[0:3])}")
