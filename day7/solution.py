from dataclasses import dataclass
from enum import Enum
from typing import Self


class CommandType(Enum):
    cd = 1
    ls = 2


@dataclass
class Command:
    cmd_type: CommandType
    params: list[str]


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    sub_dirs: list[Self]
    files: list[File]
    parent_dir: Self | None

    def sub_dir_names(self) -> list[str]:
        return [x.name for x in self.sub_dirs]

    def get_subdir(self, name):
        for x in self.sub_dirs:
            if x.name == name:
                return x
        return None

    def add_child(self, child):
        if isinstance(child, Directory):
            child.parent = self
            self.sub_dirs.append(child)
        elif isinstance(child, File):
            self.files.append(child)
    
    def size(self):
        size_of_dirs = sum([x.size() for x in self.sub_dirs])
        size_of_files = sum([x.size for x in self.files])
        return size_of_dirs + size_of_files


def parse_command_line(line: str):
    if line.startswith("cd"):
        return Command(cmd_type=CommandType.cd, params=line[3:].split())
    elif line.startswith("ls"):
        return Command(cmd_type=CommandType.ls, params=line[3:].split())
    return None

def parse_ls_line(line: str):
    left, right = line.split(" ")
    if left == "dir":
        return Directory(name=right, sub_dirs=[], files=[], parent_dir=None)
    elif left.isdigit():
        return File(name=right, size=int(left))
    return None




def part1(root: Directory):
    def find_target_dirs(dir, acc):
        if dir.size() <= 100000:
            acc += dir.size()
        for x in dir.sub_dirs:
            acc = find_target_dirs(x, acc)
        return acc
    print(find_target_dirs(root, 0))


def part2(root: Directory):
    disk_space = 70000000
    free_space = disk_space - root.size()
    required_space = 30000000 - free_space

    def find_optimal_dir_size(dir, result_space, required_space):
        optimal_size = result_space
        if dir.size() >= required_space and dir.size() < result_space:
            optimal_size = dir.size()
        for d in dir.sub_dirs:
            optimal_size = find_optimal_dir_size(d, optimal_size, required_space)
        return optimal_size
    print(find_optimal_dir_size(root, disk_space, required_space))


def main():
    file_content = ""
    with open("input.txt") as f:
        file_content = f.read()
    
    root = Directory(name="/", sub_dirs=[], files=[], parent_dir=None)
    current = None
    for line in file_content.split("\n"):
        if line.startswith("$"):
            cmd = parse_command_line(line[2:])
            if cmd.cmd_type == CommandType.cd:
                if not cmd.params:
                    # Throw Error
                    continue
                cd_into = cmd.params[0]
                if cd_into == "/":
                    current = root
                elif cd_into == "..":
                    current = current.parent
                elif cd_into in current.sub_dir_names():
                    current = current.get_subdir(cd_into)
                else:
                    # Throw Error
                    continue
            elif cmd.cmd_type == CommandType.ls:
                pass
        else:
            current.add_child(parse_ls_line(line))
    
    part1(root)
    part2(root)


if __name__ == "__main__":
    main()
