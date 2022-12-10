from dataclasses import dataclass, field
from enum import Enum


DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1)
}

counter = 0

@dataclass
class Point:
    x: int = 0
    y: int = 0
    mileage: int = 0
    path: list[tuple[int, int]] = field(default_factory=lambda:[0, 0])

    def move(self, direction: str):
        move_x, move_y = DIRECTIONS[direction]
        self.x += move_x
        self.y += move_y
        self.mileage += 1
    
    def should_chase(self, destination):
        return not (abs(self.x - destination.x) <= 1 and abs(self.y - destination.y) <= 1)

    def chase(self, destination):        
        if self.should_chase(destination):
            y_dist = abs(destination.y - self.y)
            x_dist = abs(destination.x - self.x)
            y_dir = "D" if destination.y > self.y else "U"
            x_dir = "R" if destination.x > self.x else "L"
            if x_dist > 0:
                self.move(x_dir)
            if y_dist > 0:
                self.move(y_dir)
            self.path.append((self.x, self.y))


def part1(file_content: str):
    head = Point()
    tail = Point()
    for motion in file_content.split("\n"):
        mov_dir, mov_len = motion[0], int(motion[1:])
        for _ in range(mov_len):
            head.move(mov_dir)
            tail.chase(head)
    
    print(len(set(tail.path)))


def part2(file_content: str):
    pass


def main():
    file_content = ""
    with open("day9/input.txt") as f:
        file_content = f.read()
    
    part1(file_content)
    part2(file_content)


if __name__ == "__main__":
    main()
