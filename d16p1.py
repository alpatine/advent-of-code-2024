from collections import deque


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

def find_lowest_score(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    start, end = find_ends(grid)
    to_check = deque()
    to_check.append((end, (-1, 0), 0))
    to_check.append((end, (0, -1), 0))

    grid_costs = [[-1 for c in range(width)] for r in range(height)]

    while to_check:
        (r, c), (dr, dc), score = pos, dir, score = to_check.popleft()

        # don't explore further if our path is more expensive
        if grid_costs[r][c] != -1 and grid_costs[r][c] < score: continue
        grid_costs[r][c] = score

        # can we go straight?
        next_r, next_c = r+dr, c+dc
        if grid[next_r][next_c] in '.S':
            to_check.append(((next_r, next_c), (dr, dc), score + 1))

        # can we go left?
        tdr, tdc = turn_left((dr, dc))
        next_r, next_c = r + tdr, c + tdc
        if grid[next_r][next_c] in '.S':
            to_check.append(((next_r, next_c), (tdr, tdc), score + 1001))

        # can we go right?
        tdr, tdc = -tdr, -tdc # right is opposite of left
        next_r, next_c = r + tdr, c + tdc
        if grid[next_r][next_c] in '.S':
            to_check.append(((next_r, next_c), (tdr, tdc), score + 1001))
    
    smallest_score = grid_costs[start[0]][start[1]]
    return smallest_score


def d16p1(data: str) -> int:
    grid = parseData(data)
    score = find_lowest_score(grid)
    return score
    
if __name__ == '__main__':
    data = readDataFile()
    result = d16p1(data)
    print(result)
