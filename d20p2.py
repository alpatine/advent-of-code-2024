from itertools import combinations


def readDataFile() -> str:
    with open('d20data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    grid = [[c for c in line] for line in data.splitlines()]
    return grid

def find_start(grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'S': return (row_index, col_index)

def find_path(grid: list[list[str]], start: tuple[int, int]) -> list[tuple[tuple[int, int], int]]:
    path = []
    steps = 0

    visited = set()
    explore = start

    while explore:
        path.append((explore, steps))
        steps += 1
        

        r, c = explore
        visited.add((r, c))
        if grid[r][c] == 'E':
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and grid[nr][nc] in '.E':
                explore = (nr, nc)
                break
        else:
            explore = None
    
    return path

def find_cheats(path: list[tuple[tuple[int, int], int]]) -> list[tuple[tuple[int, int], tuple[int, int], int]]:
    cheats = []

    for (start, end) in combinations(path, 2):
        (sr, sc), s_steps = start
        (er, ec), e_steps = end
        dist = abs(er - sr) + abs(ec - sc)
        if dist <= 20 and s_steps + dist < e_steps:
            cheats.append(((sr, sc), (er, ec), e_steps - s_steps - dist))

    return cheats

def d20p2(data: str, threshold: int) -> str:
    grid = parseData(data)
    start = find_start(grid)
    path = find_path(grid, start)
    cheats = find_cheats(path)

    wanted_cheats = 0
    for _, _, steps in cheats:
        if steps >= threshold:
            wanted_cheats += 1

    return wanted_cheats
    
if __name__ == '__main__':
    data = readDataFile()
    result = d20p2(data, 100)
    print(result)
