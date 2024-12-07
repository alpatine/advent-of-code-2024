from collections import Counter
from itertools import chain


def readDataFile() -> str:
    with open('d06data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def find_guard(grid: list[list[str]]) -> tuple[list[int, int], list[int, int]]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            match col:
                case '^': return [row_index, col_index], [-1, 0]
                case '>': return [row_index, col_index], [0, 1]
                case 'v': return [row_index, col_index], [1, 0]
                case '<': return [row_index, col_index], [0, -1]

def walk_grid(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    visited = [[False for col in range(width)] for row in range(height)]
    pos, direction = find_guard(grid)
    
    while True:
        visited[pos[0]][pos[1]] = True
        next_pos = [sum(x) for x in zip(pos, direction)]
        if 0 <= next_pos[0] < height and 0 <= next_pos[1] < width:
            if grid[next_pos[0]][next_pos[1]] == '#':
                # Turn right
                direction = [direction[1], -direction[0]]
            else:
                pos = next_pos
        else: break

    return Counter(chain.from_iterable(visited))[True]

def d06p1(data: str) -> int:
    grid = parseData(data)
    visited_spaces = walk_grid(grid)
    return visited_spaces

if __name__ == '__main__':
    data = readDataFile()
    result = d06p1(data)
    print(result)