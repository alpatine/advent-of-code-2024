def readDataFile() -> str:
    with open('d15data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> tuple[list[list[str]], str]:
    grid_lines, steps_lines = data.split('\n\n')
    grid = [[c for c in line] for line in grid_lines.splitlines()]
    steps = ''.join(steps_lines.splitlines())
    return grid, steps

def find_robot(grid: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '@':
                return row_index, col_index
            
def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(''.join(line))

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
        elif grid[look_r][look_c] == 'O':
            while grid[look_r][look_c] == 'O':
                look_r += dr
                look_c += dc
            # If they finish with an empty cell, move; if a wall, end.
            if grid[look_r][look_c] == '#': continue
            elif grid[look_r][look_c] == '.':
                grid[look_r][look_c] = 'O'
                grid[robot_r + dr][robot_c + dc] = '@'
                grid[robot_r][robot_c] = '.'
                robot = robot_r + dr, robot_c + dc
    #print_grid(grid)

def calculate_gps_sum(grid: list[list[str]]) -> int:
    gps_sum = 0
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'O':
                gps = 100*row_index + col_index
                gps_sum += gps
    return gps_sum

def d15p1(data: str) -> int:
    grid, steps = parseData(data)
    robot = find_robot(grid)
    walk_grid(grid, robot, steps)
    result = calculate_gps_sum(grid)
    return result
    
if __name__ == '__main__':
    data = readDataFile()
    result = d15p1(data)
    print(result)