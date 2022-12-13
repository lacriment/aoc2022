def part1(file_content: str):
    total_strength = 0
    counter = 0
    x = 1
    
    def increment_counter():
        nonlocal total_strength
        nonlocal counter
        counter += 1
        if len(checks) and checks[0] == counter:
            total_strength += (counter * x)
            checks.pop(0)

    
    checks = [20, 60, 100, 140, 180, 220]
    for line in file_content.split("\n"):
        if line == "noop":
            increment_counter()
        elif line.startswith("addx"):
            add_val = int(line[5:])
            increment_counter()
            increment_counter()
            x += add_val
        else:
            raise NotImplementedError
    print(total_strength)


def part2(file_content: str):
    sprites = [["." for _ in range(40)] for _ in range(6)]

    counter = 0
    x = 1
    
    def increment_counter():
        nonlocal counter
        nonlocal sprites
        row = counter // 40
        col = counter % 40
        counter += 1
        if col >= x - 1 and col <= x + 1:
            sprites[row][col] = "#"
        

    
    for line in file_content.split("\n"):
        if line == "noop":
            increment_counter()
        elif line.startswith("addx"):
            add_val = int(line[5:])
            increment_counter()
            increment_counter()
            x += add_val
        else:
            raise NotImplementedError
    for row in sprites:
        for c in row:
            print(c, end="")
        print("")
    pass

    


def main():
    file_content = ""
    with open("day10/input.txt") as f:
        file_content = f.read()
    
    part1(file_content)
    part2(file_content)


if __name__ == "__main__":
    main()
