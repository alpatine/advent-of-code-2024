from collections import defaultdict, deque
from itertools import chain


def readDataFile() -> str:
    with open('d16data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    grid = [[c for c in line] for line in data.splitlines()]
    return grid

def find_ends(grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            match col:
                case 'S': start = (row_index, col_index)
                case 'E': end = (row_index, col_index)
    
    return start, end

def turn_left(d: tuple[int, int]) -> tuple[int, int]:
    return -d[1], d[0]

def turn_right(d: tuple[int, int]) -> tuple[int, int]:
    return d[1], -d[0]
            
def print_cells(grid: list[list[str]], cells: set[tuple[int, int]]) -> None:
    new_grid = [[c for c in r] for r in grid]
    for (r, c) in cells:
        new_grid[r][c] = 'O'
    for line in new_grid:
        print(''.join(line))

def find_lowest_score(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    start, end = find_ends(grid)
    to_check = deque()
    to_check.append((end, (0, -1), 0, [[]]))
    to_check.append((end, (1, 0), 0, [[]]))

    grid_costs = [[defaultdict(lambda: -1) for c in range(width)] for r in range(height)]

    complete_paths = defaultdict(list)

    while to_check:
        pos, dir, score, paths = to_check.popleft()
        r, c = pos
        dr, dc = dir

        # are we in a loop
        loop = [path for path in paths if pos in path]
        if len(loop) > 1: continue

        new_paths = [path + [pos] for path in paths]

        # are we at the end?
        if grid[r][c] == 'S':
            complete_paths[score] += new_paths

        # can we go straight?
        next_r, next_c = r+dr, c+dc
        if grid[next_r][next_c] in '.S' and (grid_costs[r][c][dr, dc] == -1 or grid_costs[r][c][dr, dc] >= score+1):
            grid_costs[r][c][dr, dc] = score+1
            to_check.append(((next_r, next_c), (dr, dc), score + 1, new_paths))

        # can we go left?
        tdr, tdc = turn_left((dr, dc))
        next_r, next_c = r + tdr, c + tdc
        if grid[next_r][next_c] in '.S' and (grid_costs[r][c][dr, dc] == -1 or grid_costs[r][c][dr, dc] >= score):
            grid_costs[r][c][dr, dc] = score+1001
            to_check.append(((next_r, next_c), (tdr, tdc), score + 1001, new_paths))

        # can we go right?
        tdr, tdc = -tdr, -tdc # right is opposite of left
        next_r, next_c = r + tdr, c + tdc
        if grid[next_r][next_c] in '.S' and (grid_costs[r][c][dr, dc] == -1 or grid_costs[r][c][dr, dc] >= score):
            grid_costs[r][c][dr, dc] = score+1001
            to_check.append(((next_r, next_c), (tdr, tdc), score + 1001, new_paths))
    
    smallest_score = min(complete_paths.keys())
    cells = set(chain.from_iterable(complete_paths[smallest_score]))
    #print_cells(grid, cells)

    return len(cells)

def d16p2(data: str) -> int:
    grid = parseData(data)
    score = find_lowest_score(grid)
    return score
    
if __name__ == '__main__':
    data = readDataFile()
    result = d16p2(data)
    print(result)
