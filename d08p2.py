from collections import defaultdict
from itertools import combinations

def readDataFile() -> str:
    with open('d08data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def find_antennae(grid: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    locations = defaultdict(list)
    for row_id, row in enumerate(grid):
        for col_id, col in enumerate(row):
            if col != '.':
                locations[col].append((row_id, col_id))
    return locations

def in_bounds(grid: list[list[str]], location: tuple[int, int]) -> bool:
    height = len(grid)
    width = len(grid[0])
    return 0 <= location[0] < height and 0 <= location[1] < width

def find_antinodes(grid: list[list[str]], antenna_locations: list[tuple[int, int]]) -> list[tuple[int, int]]:
    antinode_locations = []
    for pair in combinations(antenna_locations, 2):
        # dist is a vector from pair[1] to pair[0]
        dist = (pair[0][0]-pair[1][0], pair[0][1]-pair[1][1])

        step = 1
        while True:            
            # add to pair[1] and check bounds
            possible_location = (pair[1][0] + step*dist[0], pair[1][1] + step*dist[1])
            if in_bounds(grid, possible_location): antinode_locations.append(possible_location)
            else: break
            step += 1

        step = 1
        while True:
            # subtract from pair[0] and check bounds
            possible_location = (pair[0][0] - step*dist[0], pair[0][1] - step*dist[1])
            if in_bounds(grid, possible_location): antinode_locations.append(possible_location)
            else: break
            step += 1
    
    return antinode_locations

def count_antinode_locations(grid: list[list[str]]) -> int:
    antinode_locations = set()
    
    antennae = find_antennae(grid)
    for antenna_locations in antennae.values():
        antinode_locations.update(find_antinodes(grid, antenna_locations))

    return len(antinode_locations)

def d08p2(data: str) -> int:
    grid = parseData(data)
    antinode_count = count_antinode_locations(grid)
    return antinode_count
    
if __name__ == '__main__':
    data = readDataFile()
    result = d08p2(data)
    print(result)
