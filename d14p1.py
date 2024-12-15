from collections import defaultdict
import re

def readDataFile() -> str:
    with open('d14data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    robots = []
    for line in data.splitlines():
        match = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        robot = ((int(match[1]), int(match[2])), (int(match[3]), int(match[4])))
        robots.append(robot)
    return robots

def step(pos: tuple[int, int], vel: tuple[int, int], width: int, height: int, steps: int) -> tuple[int, int]:
    new_pos_x = (pos[0] + vel[0] * steps) % width
    new_pos_y = (pos[1] + vel[1] * steps) % height
    return new_pos_x, new_pos_y

def find_quad(pos: tuple[int, int], width: int, height: int) -> int:
    mid_x = width // 2
    mid_y = height // 2
    x, y = pos

    if x > mid_x and y < mid_y: return 1
    if x < mid_x and y < mid_y: return 2
    if x < mid_x and y > mid_y: return 3
    if x > mid_x and y > mid_y: return 4

    return 0

def d14p1(data: str, width: int, height: int) -> int:
    new_positions = []
    quads = defaultdict(int)
    safety_factor = 1
    robots = parseData(data)
    for pos, vel in robots:
        new_pos = step(pos, vel, width, height, 100)
        new_positions.append(new_pos)
    for pos in new_positions:
        quad = find_quad(pos, width, height)
        if quad != 0: quads[quad] += 1
    for count in quads.values():
        safety_factor *= count
    return safety_factor
    
if __name__ == '__main__':
    data = readDataFile()
    result = d14p1(data, 101, 103)
    print(result)
