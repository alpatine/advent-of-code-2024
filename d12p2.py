from collections import defaultdict


class Region:
    def __init__(self):
        self.plots = []
        self.north_borders = []
        self.east_borders = []
        self.south_borders = []
        self.west_borders = []
        self.sides = 0

class Plot:
    def __init__(self):
        self.visited = False

def readDataFile() -> str:
    with open('d12data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def explore_region(grid: list[list[str]], region: Region, r: int, c: int, visited_plots: dict[tuple[int, int], Plot]) -> None:
    height = len(grid)
    width = len(grid[0])

    plot = visited_plots[(r,c)]
    region.plots.append(plot)

    plot.visited = True

    region_type = grid[r][c]

    for (delta_r, delta_c, borders) in [
            (-1, 0, region.north_borders),
            (0, 1, region.east_borders),
            (1, 0, region.south_borders),
            (0, -1, region.west_borders)]:
        next_r = r+delta_r
        next_c = c+delta_c
        if 0 <= next_r < height and 0 <= next_c < width and grid[next_r][next_c] == region_type:
            if not visited_plots[(next_r,next_c)].visited:
                explore_region(grid, region, next_r, next_c, visited_plots)
        else:
            borders.append((r, c))

def count_runs(table: dict[int, list[int]]) -> int:
    sides = 0
    for r, c_list in table.items():
        c_list.sort()
        last_seen = -2
        for c in c_list:
            if c != last_seen + 1:
                sides += 1
            last_seen = c
    return sides

def count_sides(region: Region):
    for borders, horizontal in [
            (region.north_borders, True),
            (region.south_borders, True),
            (region.east_borders, False),
            (region.west_borders, False)]:
        border_rows = defaultdict(list)
        for r, c in borders:
            if horizontal: border_rows[r].append(c)
            else: border_rows[c].append(r)
        region.sides += count_runs(border_rows)

def calculate_total_price(grid: list[list[str]]) -> None:
    height = len(grid)
    width = len(grid[0])

    total_price = 0
    visited_plots = defaultdict(Plot)

    for r in range(height):
        for c in range(width):
            if not visited_plots[r, c].visited:
                region = Region()
                explore_region(grid, region, r, c, visited_plots)
                count_sides(region)
                total_price += region.sides * len(region.plots)
    return total_price

def d12p2(data: str) -> int:
    grid = parseData(data)
    total_price = calculate_total_price(grid)
    return total_price
    
if __name__ == '__main__':
    data = readDataFile()
    result = d12p2(data)
    print(result)
