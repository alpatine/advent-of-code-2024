from collections import deque


def readDataFile() -> str:
    with open('d15data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> tuple[list[list[str]], str]:
    grid_lines, steps_lines = data.split('\n\n')
    grid = [[c for c in line] for line in grid_lines.splitlines()]
    steps = ''.join(steps_lines.splitlines())
    return grid, steps

def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(''.join(line))

def transform_grid(input: list[list[str]]) -> list[list[str]]:
    height = len(input)
    width = len(input[0])
    
    #print_grid(input)
    output = [['.' for c in range(width*2)] for r in range(height)]

    for r in range(height):
        for c in range(width):
            
            match input[r][c]:
                case '#': output[r][c*2:c*2+2] = '##'
                case 'O': output[r][c*2:c*2+2] = '[]'
                case '.': output[r][c*2:c*2+2] = '..'
                case '@': output[r][c*2:c*2+2] = '@.'

    #print_grid(output)
    return output

def find_robot(grid: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '@':
                return row_index, col_index 
            
def push_horizontal(grid: list[list[str]], robot: tuple[int, int], dc: int) -> tuple[int, int]:
    robot_r, robot_c = robot
    look_r = robot_r
    look_c = robot_c + dc
    
    while grid[look_r][look_c] in '[]':
        look_c += dc
    if grid[look_r][look_c] == '#': return robot
    elif grid[look_r][look_c] == '.':
        while look_c != robot_c:
            grid[look_r][look_c], grid[look_r][look_c - dc] = grid[look_r][look_c - dc], grid[look_r][look_c]
            look_c -= dc
        return robot_r, robot_c + dc

def push_vertical(grid: list[list[str]], robot: tuple[int, int], dr: int) -> tuple[int, int]:
    check_cells = deque()
    checked = set()
    push_cells = deque()
    pushed = set()

    check_cells.append(robot)

    while check_cells:
        r, c = check_cells.popleft()
        if (r, c) in checked: continue
        
        next_r = r + dr
        match grid[next_r][c]:
            case '#': return robot
            case '[':
                check_cells.append((next_r, c))
                check_cells.append((next_r, c+1))
            case ']':
                check_cells.append((next_r, c-1))
                check_cells.append((next_r, c))
        
        checked.add((r, c))
        push_cells.append((r, c))
    
    while push_cells:
        r, c = push_cells.pop()
        if (r, c) in pushed: continue

        next_r = r + dr
        grid[r][c], grid[next_r][c] = grid[next_r][c], grid[r][c]

        pushed.add((r, c))

    return robot[0] + dr, robot[1]

def walk_grid(grid: list[list[str]], robot: tuple[int, int], steps: str) -> None:
    for step in steps:
        #print_grid(grid)
        match step:
            case '^': dr, dc = -1, 0
            case '>': dr, dc = 0, 1
            case 'v': dr, dc = 1, 0
            case '<': dr, dc = 0, -1

        robot_r,robot_c = robot
        look_r = robot_r + dr
        look_c = robot_c + dc
        
        # if the next cell is empty, move there
        if grid[look_r][look_c] == '.':
            grid[look_r][look_c] = '@'
            grid[robot_r][robot_c] = '.'
            robot = look_r, look_c
            continue

        # if not, if it's a wall, end
        elif grid[look_r][look_c] == '#':
            continue

        # if not, it's a box, work out when the run of boxes finishes
        elif grid[look_r][look_c] in '[]':
            
            # Are we going horizontal
            if dr == 0:
                robot = push_horizontal(grid, robot, dc)
            else:
                robot = push_vertical(grid, robot, dr)

def calculate_gps_sum(grid: list[list[str]]) -> int:
    gps_sum = 0
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '[':
                gps = 100*row_index + col_index
                gps_sum += gps
    return gps_sum

def d15p2(data: str) -> int:
    grid, steps = parseData(data)
    grid = transform_grid(grid)
    robot = find_robot(grid)
    walk_grid(grid, robot, steps)
    result = calculate_gps_sum(grid)
    return result
    
if __name__ == '__main__':
    data = readDataFile()
    result = d15p2(data)
    print(result)