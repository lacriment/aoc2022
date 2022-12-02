file_content = ""
with open("input.txt") as f:
    file_content = f.read()

scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

choices = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

guide = [x.split(' ') for x in file_content.split('\n')]

total = 0
for game in guide:
    opp = choices[game[0]]
    me = choices[game[1]]
    if opp == me:
        total += (3 + scores[me])
    if opp == "rock":
        if me == "scissors":
            total += (0 + scores[me])
        if me == "paper":
            total += (6 + scores[me])
    if opp == "paper":
        if me == "rock":
            total += (0 + scores[me])
        if me == "scissors":
            total += (6 + scores[me])
    if opp == "scissors":
        if me == "rock":
            total += (6 + scores[me])
        if me == "paper":
            total += (0 + scores[me])
print(total)

second_total = 0
for game in guide:
    opp = choices[game[0]]
    me = choices[game[1]]
    game[1]
    if game[1] == 'X':
        if opp == "rock":
            second_total += scores["scissors"] + 0
        if opp == "paper":
            second_total += scores["rock"] + 0
        if opp == "scissors":
            second_total += scores["paper"] + 0
    if game[1] == 'Y':
        second_total += scores[opp] + 3
    if game[1] == 'Z':
        if opp == "rock":
            second_total += scores["paper"] + 6
        if opp == "paper":
            second_total += scores["scissors"] + 6
        if opp == "scissors":
            second_total += scores["rock"] + 6
print(second_total)