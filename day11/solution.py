def run_operation(operation, val):
    left_val = val if operation[0] == "old" else int(operation[0])
    operand = operation[1]
    right_val = val if operation[2] == "old" else int(operation[2])
    if operand == "*":
        return left_val * right_val
    elif operand == "+":
        return left_val + right_val
    else:
        raise NotImplementedError

def part1(file_content: str):
    monkeys = []
    try:
        for text in file_content.split("\n\n"):
            lines = text.split("\n")
            m = {
                "items": [int(x) for x in lines[1][18:].split(', ')],
                "operation": lines[2][19:].split(' '),
                "divisible_by": int(lines[3][21:]),
                True: int(lines[4][29:]),
                False: int(lines[5][30:]),
                "inspected": 0
            }
            monkeys.append(m)
    except ValueError:
        print("Parsing Error")
    
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey["items"]):
                x = monkey["items"].pop(0)
                x = run_operation(monkey["operation"], x)
                x //= 3
                b = (x % monkey["divisible_by"] == 0)
                monkeys[monkey[b]]["items"].append(x)
                monkey["inspected"] += 1
    
    for i in range(len(monkeys)):
        print(f"Monkey {i} inspected items {monkeys[i]['inspected']} times.")
    
    inspection_rates = sorted([x["inspected"] for x in monkeys], reverse=True)
    print(inspection_rates[0] * inspection_rates[1])






def part2(file_content: str):
    monkeys = []
    try:
        for text in file_content.split("\n\n"):
            lines = text.split("\n")
            m = {
                "items": [int(x) for x in lines[1][18:].split(', ')],
                "operation": lines[2][19:].split(' '),
                "divisible_by": int(lines[3][21:]),
                True: int(lines[4][29:]),
                False: int(lines[5][30:]),
                "inspected": 0
            }
            monkeys.append(m)
    except ValueError:
        print("Parsing Error")
    
    mod_with = 1
    for x in monkeys:
        mod_with *= x["divisible_by"]
    for _ in range(10000):
        for monkey in monkeys:
            while len(monkey["items"]):
                x = monkey["items"].pop(0)
                x = run_operation(monkey["operation"], x)
                x %= mod_with
                b = (x % monkey["divisible_by"] == 0)
                monkeys[monkey[b]]["items"].append(x)
                monkey["inspected"] += 1
    
    print("------------PART2----------")
    for i in range(len(monkeys)):
        print(f"Monkey {i} inspected items {monkeys[i]['inspected']} times.")
        
    inspection_rates = sorted([x["inspected"] for x in monkeys], reverse=True)
    print(inspection_rates[0] * inspection_rates[1])


def main():
    file_content = ""
    with open("day11/input.txt") as f:
        file_content = f.read()
    
    part1(file_content)
    part2(file_content)


if __name__ == '__main__':
    main()
