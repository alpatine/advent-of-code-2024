from collections import defaultdict


def readDataFile() -> str:
    with open('d12data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[str]:
    return [[char for char in line] for line in data.splitlines()]

def explore_region(grid: list[list[str]], r: int, c: int, visited: defaultdict[tuple[int, int], bool]) -> tuple[int, int, int]:
    height = len(grid)
    width = len(grid[0])

    visited[(r, c)] = True
    
    region_type = grid[r][c]
    region_perimeter = 0
    region_area = 1

    for (delta_r, delta_c) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        next_r = r+delta_r
        next_c = c+delta_c
        if 0 <= next_r < height and 0 <= next_c < width and grid[next_r][next_c] == region_type:
            if not visited[(next_r,next_c)]:
                next_region_perimeter, next_region_area = explore_region(grid, next_r, next_c, visited)
                region_perimeter += next_region_perimeter
                region_area += next_region_area                
        else:
            region_perimeter += 1

    return region_perimeter, region_area
    

def calculate_total_price(grid: list[list[str]]) -> None:
    height = len(grid)
    width = len(grid[0])

    total_price = 0

    visited = defaultdict(bool)

    for r in range(height):
        for c in range(width):
            if not visited[r, c]:
                perimeter, area = explore_region(grid, r, c, visited)
                total_price += perimeter * area
    return total_price


def d12p1(data: str) -> int:
    grid = parseData(data)
    total_price = calculate_total_price(grid)
    return total_price
    
if __name__ == '__main__':
    data = readDataFile()
    result = d12p1(data)
    print(result)
