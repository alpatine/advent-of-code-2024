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

def find_cheats(grid: list[list[str]], path: list[tuple[tuple[int, int], int]]) -> list[tuple[tuple[int, int], tuple[int, int], int]]:
    height = len(grid)
    width = len(grid[0])
    step_counts = {(r, c): step_count for (r, c), step_count in path}
    cheats = []

    deltas = [
        ((0, 2), (0, 1)),
        ((2, 0), (1, 0)),
        ((0, -2), (0, -1)),
        ((-2, 0), (-1, 0)),
    ]
    
    for (r, c), steps in path:
        # need to check cells that have manhattan distance of 2 away, and a wall in the way
        for delta in deltas:
            (check_dr, check_dc), (wall_dr, wall_dc) = delta
            check_r, check_c, wall_r, wall_c = r + check_dr, c + check_dc, r + wall_dr, c + wall_dc
            if 0 <= check_r < height and 0 <= check_c < width:
                if (check_r, check_c) in step_counts:
                    check_steps = step_counts[check_r, check_c]
                    if check_steps > steps and grid[wall_r][wall_c] == '#':
                        cheats.append(((r, c), (check_r, check_c), check_steps-steps-2))

    return cheats

def d20p1(data: str, threshold: int) -> str:
    grid = parseData(data)
    start = find_start(grid)
    path = find_path(grid, start)
    cheats = find_cheats(grid, path)
    
    wanted_cheats = 0
    for _, _, steps in cheats:
        if steps >= threshold:
            wanted_cheats += 1

    return wanted_cheats
    
if __name__ == '__main__':
    data = readDataFile()
    result = d20p1(data, 100)
    print(result)
