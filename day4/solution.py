def part1(file_content: str):
    pairs = file_content.split('\n')
    counter = 0
    for pair in pairs:
        left, right = [x.split('-') for x in pair.split(',')]
        a, b, c, d = int(left[0]), int(left[1]), int(right[0]), int(right[1])
        if a <= c and b >= d:
            counter += 1
        elif a >= c and b <= d:
            counter += 1
    print(counter)


def part2(file_content: str):
    pairs = file_content.split('\n')
    counter = 0
    for pair in pairs:
        left, right = [x.split('-') for x in pair.split(',')]
        a, b, c, d = int(left[0]), int(left[1]), int(right[0]), int(right[1])
        if b >= c and a <= d:
            counter += 1
    print(counter)


def main():
    file_content = ""
    with open("input.txt") as f:
        file_content = f.read()
    part1(file_content)
    part2(file_content)


if __name__ == "__main__":
    main()