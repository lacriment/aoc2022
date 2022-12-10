from dataclasses import dataclass, field
from enum import Enum
from typing import Self


DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "X": (0, 0)
}


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@dataclass
class Knot(Point):
    path: list[Point] = field(default_factory=lambda:[Point()])

    def move(self, direction: str|None):
        if direction != "X":
            move_x, move_y = DIRECTIONS[direction]
            self.x += move_x
            self.y += move_y
    
    def should_chase(self, destination):
        return not (abs(self.x - destination.x) <= 1 and abs(self.y - destination.y) <= 1)

    def chase(self, destination):
        if self.should_chase(destination):
            y_dir = 'X' if destination.y == self.y else ("D" if destination.y > self.y else "U")
            x_dir = 'X' if destination.x == self.x else ("R" if destination.x > self.x else "L")
            self.move(x_dir)
            self.move(y_dir)
            self.path.append(Point(x=self.x, y=self.y))


def visualize(points: list[Point]):
    if not len(points):
        return
    x_max = max([p.x for p in points])
    x_min = min([p.x for p in points])
    y_max = max([p.y for p in points])
    y_min = min([p.y for p in points])
    len_x = abs(x_max) + abs(x_min)
    len_y = abs(y_max) + abs(y_min)
    table = [["-" for _ in range(len_x + 1)] for _ in range(len_y + 1)]
    for p in points:
        x = (p.x) - x_min
        y = (p.y) - y_min
        table[y][x] = "O"
    for row in table:
        for item in row:
            print(f" {item} ", end="")
        print("\n")


def part1(file_content: str):
    head = Knot()
    tail = Knot()
    for motion in file_content.split("\n"):
        mov_dir, mov_len = motion[0], int(motion[1:])
        for _ in range(mov_len):
            head.move(mov_dir)
            tail.chase(head)
    
    print(len(set(tail.path)))


def part2(file_content: str):
    TAIL_LENGTH = 9
    head = Knot()
    tail = [Knot() for _ in range(TAIL_LENGTH)]
    for motion in file_content.split("\n"):
        mov_dir, mov_len = motion[0], int(motion[1:])
        for _ in range(mov_len):
            head.move(mov_dir)
            tail[0].chase(head)
            for i in range(1, TAIL_LENGTH):
                tail[i].chase(tail[i-1])

    print(len(set(tail[TAIL_LENGTH-1].path)))


def main():
    file_content = ""
    with open("day9/input.txt") as f:
        file_content = f.read()
    
    part1(file_content)
    part2(file_content)


if __name__ == "__main__":
    main()
