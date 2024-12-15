import re

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f'x={self.x} y={self.y} vx={self.vx} vy={self.vy}'
    
    def step(self, steps: int, width: int, height: int) -> None:
        self.x = (self.x + self.vx * steps) % width
        self.y = (self.y + self.vy * steps) % height

def readDataFile() -> str:
    with open('d14data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[Robot]:
    robots = []
    for line in data.splitlines():
        match = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        robot = Robot(int(match[1]), int(match[2]), int(match[3]), int(match[4]))
        robots.append(robot)
    return robots

def check_tree(robots: list[Robot], width: int, height: int) -> bool:
    grid = [['.' for x in range(width)] for y in range(height)]
    for robot in robots:
        grid[robot.y][robot.x] = '#'

    run_found = False
    for line in grid:
        line = ''.join(line)
        if line.find('##########') > -1:
            run_found = True
            break
    
    return run_found

def print_robots(robots: list[Robot], width: int, height: int) -> None:
    grid = [['.' for x in range(width)] for y in range(height)]
    for robot in robots:
        grid[robot.y][robot.x] = '#'
    for r in range(height):
        print(''.join(grid[r]))

def d14p2(data: str, width: int, height: int, print_solution: bool) -> int:
    robots = parseData(data)

    steps = 0
    while not check_tree(robots, width, height):
        for robot in robots:
            robot.step(1, width, height)
        steps += 1

    if print_solution: print_robots(robots, width, height)

    return steps
    
if __name__ == '__main__':
    data = readDataFile()
    result = d14p2(data, 101, 103, True)
    print(result)
