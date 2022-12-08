def part1(forest, row_count, column_count):
    visibility_matrix = []
    visible_count = 0
    for i in range(row_count):
        l = []
        for j in range(column_count):
            if i == 0 or j == 0 or i == row_count-1 or j == column_count-1:
                l.append((True, True, True, True))
                visible_count += 1
                continue
            
            left = True
            right = True
            top = True
            bottom = True

            the_item = forest[i][j]

            # left
            x = j - 1
            while x >= 0:
                if forest[i][x] >= the_item:
                    left = False
                x -= 1
            
            # right
            x = j + 1
            while x < column_count:
                if forest[i][x] >= the_item:
                    right = False
                x += 1
            
            # top
            x = i - 1
            while x >= 0:
                if forest[x][j] >= the_item:
                    top = False
                x -= 1
            
            # bottom
            x = i + 1
            while x < row_count:
                if forest[x][j] >= the_item:
                    bottom = False
                x += 1

            values = (left, right, top, bottom)
            l.append(values)
            visible_count += (1 if True in values else 0)
        visibility_matrix.append(l)
    print(visible_count)

def part2(forest, row_count, column_count):
    max_scenic_score = 0
    for i in range(row_count):
        l = []
        for j in range(column_count):
            the_item = forest[i][j]
            left = 0
            right = 0
            top = 0
            bottom = 0

            # left
            x = j - 1
            while x >= 0:
                left += 1
                if forest[i][x] >= the_item:
                    break
                x -= 1                
            
            # right
            x = j + 1
            while x < column_count:
                right += 1
                if forest[i][x] >= the_item:
                    break
                x +=1            
            
            # top
            x = i - 1
            while x >= 0:
                top += 1
                if forest[x][j] >= the_item:
                    break
                x -= 1
            
            # bottom
            x = i + 1
            while x < row_count:
                bottom += 1
                if forest[x][j] >= the_item:
                    break
                x += 1
            
            scenic_score = (left * right * top * bottom)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(max_scenic_score)


def main():
    file_content = ""
    with open("input.txt") as f:
        file_content = f.read()
    
    forest = []
    row_count = 0
    column_count = 0
    for row in file_content.split('\n'):
        l = []
        for item in row:
            l.append(int(item))
        forest.append(l)
        row_count += 1
    column_count = len(forest[0])
    
    part1(forest, row_count, column_count)
    part2(forest, row_count, column_count)


if __name__ == '__main__':
    main()
