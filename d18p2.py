import sys
from collections import defaultdict, deque
from queue import PriorityQueue


class Cell:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.dist_to_end = 0
        self.prev = None

    def __repr__(self):
        return f'x={self.x} y={self.y} dist={self.dist_to_end}'

    def __lt__(self, value):
        return self.dist_to_end < value.dist_to_end

def readDataFile() -> str:
    with open('d18data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> deque[tuple[int, int]]:
    output = deque()
    for line in data.splitlines():
        x, y = line.split(',')
        output.append((int(x), int(y)))
    return output

def make_grid(width: int, height: int) -> list[list[str]]:
    return [['.' for x in range(width)] for y in range(height)]

def apply_bytes(grid: list[list[str]], bytes: deque[tuple[int, int]], byte_count: int) -> tuple[list[list[str]], list[tuple[int, int]]]:
    applied = []
    for _ in range(byte_count):
        if bytes:
            x, y = bytes.popleft()
            grid[y][x] = '#'
            applied.append((x, y))

    return grid, applied

def print_path(grid: list[list[str]], cell: Cell) -> None:
    height = len(grid)
    width = len(grid[0])
    new_grid = [[grid[y][x] for x in range(width)] for y in range(height)]

    while cell:
        new_grid[cell.y][cell.x] = 'O'
        cell = cell.prev

    for line in new_grid:
        print(''.join(line))

def find_shortest_path(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[Cell]:
    height, width = len(grid), len(grid[0])
    sx, sy = start[0], start[1]
    ex, ey = end[0], end[1]

    start_cell = Cell()
    start_cell.x = sx
    start_cell.y = sy
    start_cell.dist_to_end = abs(ex-sx) + abs(ey-sy)

    front_line: PriorityQueue[tuple[Cell, int]] = PriorityQueue()
    front_line.put((start_cell, 0))

    fewest_steps = defaultdict(lambda: sys.maxsize)

    while front_line.qsize() > 0:
        cell, steps = front_line.get()
        x, y = cell.x, cell.y

        # have we reached the end
        if (x, y) == (ex, ey): break

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '.' and steps+1 < fewest_steps[nx, ny]:
                fewest_steps[nx, ny] = steps+1
                next_cell = Cell()
                next_cell.x = nx
                next_cell.y = ny
                next_cell.dist_to_end = steps + abs(ex-nx) + abs(ey-ny)
                next_cell.prev = cell
                front_line.put((next_cell, steps+1))
    else:
        return None
    
    path = []
    while cell:
        path.append(cell)
        cell = cell.prev

    return path

def d18p2(data: str, byte_count: int, width: int, height: int) -> int:
    byte_positions = parseData(data)
    grid = make_grid(height, width)
    grid, _ = apply_bytes(grid, byte_positions, byte_count)
    path = find_shortest_path(grid, (0, 0), (width-1, height-1))

    while byte_positions:
        grid, last_applied = apply_bytes(grid, byte_positions, 1)
        path = find_shortest_path(grid, (0, 0), (width-1, height-1))
        if path is None:
            # it's blocked
            return last_applied[0]
    
if __name__ == '__main__':
    data = readDataFile()
    result = d18p2(data, 1024, 71, 71)
    print(result)
