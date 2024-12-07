from collections import defaultdict


def readDataFile() -> str:
    with open('d06data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def find_guard(grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            match col:
                case '^': return (row_index, col_index), (-1, 0)
                case '>': return (row_index, col_index), (0, 1)
                case 'v': return (row_index, col_index), (1, 0)
                case '<': return (row_index, col_index), (0, -1)

def walk_grid(grid: list[list[str]], guard: tuple[tuple[int, int],tuple[int,int]]) -> dict[tuple[int, int], bool]:
    height = len(grid)
    width = len(grid[0])
    visited = defaultdict(bool)
    pos, direction = guard
    
    while True:
        visited[pos] = True
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if 0 <= next_pos[0] < height and 0 <= next_pos[1] < width:
            if grid[next_pos[0]][next_pos[1]] == '#':
                # Turn right
                direction = [direction[1], -direction[0]]
            else:
                pos = next_pos
        else: break

    return visited

def check_loop(grid: list[list[str]], guard: tuple[tuple[int,int],tuple[int,int]]) -> int:
    height = len(grid)
    width = len(grid[0])
    visited = defaultdict(list)
    pos, direction = guard
    
    while True:
        if direction in visited[pos]:
            return True
        
        visited[pos].append(direction)
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if 0 <= next_pos[0] < height and 0 <= next_pos[1] < width:
            if grid[next_pos[0]][next_pos[1]] == '#':
                direction = (direction[1], -direction[0])
            else:
                pos = next_pos
        else: return False

def check_modified_grids(grid: list[list[str]]) -> int:
    loop_grid_count = 0
    guard = find_guard(grid)
    visited = walk_grid(grid, guard)

    for row, col in visited.keys():
        if grid[row][col] == '.':
            grid[row][col] = '#'
            if check_loop(grid, guard):
                loop_grid_count += 1
            grid[row][col] = '.'
    return loop_grid_count

def d06p2(data: str) -> int:
    loop_grid_count = 0
    grid = parseData(data)
    loop_grid_count = check_modified_grids(grid)
    return loop_grid_count

if __name__ == '__main__':
    data = readDataFile()
    result = d06p2(data)
    print(result)