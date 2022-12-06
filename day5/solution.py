def part1(stacks, procedures):
    for line in procedures:
        _, amount, _, _from_stack, _, _to_stack = line.split(' ')
        from_stack = int(_from_stack) - 1
        to_stack = int(_to_stack) - 1
        for _ in range(int(amount)):
            stacks[to_stack].insert(0, stacks[from_stack].pop(0))
    print(''.join([stack[0] for stack in stacks]))


def part2(stacks, procedures):
    for line in procedures:
        _, amount, _, _from_stack, _, _to_stack = line.split(' ')
        from_stack = int(_from_stack) - 1
        to_stack = int(_to_stack) - 1
        stacks[to_stack] = stacks[from_stack][0:int(amount)] + stacks[to_stack]
        stacks[from_stack] = stacks[from_stack][int(amount):]
    print(''.join([stack[0] for stack in stacks]))


def read_stacks(stacks_str):
    stack_lines = stacks_str.split('\n')
    stack_count = (len(stack_lines[0]) + 1) // 4
    stacks = [[] for _ in range(stack_count)]
    for line in stacks_str.split('\n')[:-1]:
        stack_number = 0
        l_pointer = 0
        while l_pointer <= len(line):
            r_pointer = l_pointer + 4
            item = line[l_pointer: r_pointer][1]
            if item.strip():
                stacks[stack_number].append(item)
            l_pointer += 4
            stack_number += 1
    return stacks


def main():
    file_content = ""
    with open("input.txt") as f:
        file_content = f.read()
    
    stack_str, procedures_str = file_content.split('\n\n')
    procedures = [line for line in procedures_str.split('\n')]

    part1(read_stacks(stack_str), procedures)
    part2(read_stacks(stack_str), procedures)


if __name__ == "__main__":
    main()
