file_content = ""
with open("input.txt") as f:
    file_content = f.read()

pairs = file_content.split('\n')

# Part 1
counter = 0
for pair in pairs:
    left, right = [x.split('-') for x in pair.split(',')]
    a, b, c, d = int(left[0]), int(left[1]), int(right[0]), int(right[1])
    if a <= c and b >= d:
        counter += 1
    elif a >= c and b <= d:
        counter += 1
print(counter)

# Part 2
counter = 0
for pair in pairs:
    left, right = [x.split('-') for x in pair.split(',')]
    a, b, c, d = int(left[0]), int(left[1]), int(right[0]), int(right[1])
    if b >= c and a <= d:
        counter += 1
print(counter)