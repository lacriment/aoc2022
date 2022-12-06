def part1(file_content: str):
    for i in range(len(file_content)-4):
        if len(set(file_content[i:i+4])) == 4:
            print(f"{file_content[i:i+4]}, index: {i+4}")
            return


def part2(file_content: str):
    for i in range(len(file_content)-14):
        if len(set(file_content[i:i+14])) == 14:
            print(f"{file_content[i:i+14]}, index: {i+14}")
            return


def main():
    file_content = ""
    with open("input.txt") as f:
        file_content = f.read()
    
    part1(file_content)
    part2(file_content)


if __name__ == '__main__':
    main()
