def readDataFile() -> str:
    with open('d10data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in data.splitlines()]

def find_trail_heads(grid: list[list[int]]) -> list[tuple[int, int]]:
    heads = []
    for rid, row in enumerate(grid):
        for cid, col in enumerate(row):
            if col == 0:
                heads.append((rid, cid))
    return heads

def walk_trail(grid: list[list[int]],
               pos: tuple[int, int],
               expected_altitude: int,
               visited: list[tuple[int, int]]
               ) -> set[tuple[int, int]]:
    
    # Have we been here before?
    if pos in visited: return 0
        
    # Are we still within the grid?
    row = pos[0]
    col = pos[1]
    height = len(grid)
    width = len(grid[0])
    if not (0 <= pos[0] < height and 0 <= pos[1] < width): return 0
    
    # Have we reached a peak?
    altitude = grid[row][col]
    if altitude != expected_altitude: return 0
    if altitude == 9:
        return 1

    # Next steps
    next_visited = visited + [pos]
    next_altitude = altitude + 1
    score = 0
    score += walk_trail(grid, (row - 1, col), next_altitude, next_visited) # north
    score += walk_trail(grid, (row, col + 1), next_altitude, next_visited) # east
    score += walk_trail(grid, (row + 1, col), next_altitude, next_visited) # south
    score += walk_trail(grid, (row, col - 1), next_altitude, next_visited) # west

    return score

def d10p2(data: str) -> int:
    total_score = 0
    
    grid = parseData(data)
    trail_heads = find_trail_heads(grid)
    for head in trail_heads:
        trail_score = walk_trail(grid, head, 0, [])
        total_score += trail_score

    return total_score
    
if __name__ == '__main__':
    data = readDataFile()
    result = d10p2(data)
    print(result)
