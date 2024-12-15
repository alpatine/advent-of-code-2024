import re


class Machine:
    def __init__(self):
        self.ax = 0
        self.ay = 0
        self.bx = 0
        self.by = 0
        self.px = 0
        self.py = 0
    
    def __repr__(self):
        return f'(ax={self.ax} ay={self.ay} bx={self.bx} by={self.by} px={self.px} py={self.py})'
    
    def solve(self) -> tuple[int, int]:
        D = self.ax * self.by - self.ay * self.bx
        a, ar = divmod(self.by * self.px - self.bx * self.py, D)
        b, br = divmod(self.ax * self.py - self.ay * self.px, D)

        if ar == 0 and br == 0:
            return a, b
        else:
            return 0, 0

def readDataFile() -> str:
    with open('d13data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[Machine]:
    pattern = re.compile(r'.*?X\+(\d+), Y\+(\d+).*?X\+(\d+), Y\+(\d+).*?X=(\d+), Y=(\d+)', re.DOTALL)
    machines = []
    for block in data.split('\n\n'):
        match = re.match(pattern, block)
        m = Machine()
        m.ax = int(match[1])
        m.ay = int(match[2])
        m.bx = int(match[3])
        m.by = int(match[4])
        m.px = int(match[5])
        m.py = int(match[6])
        machines.append(m)
    return machines

def d13p2(data: str) -> int:
    machines = parseData(data)

    running_cost = 0
    for machine in machines:
        machine.px += 10000000000000
        machine.py += 10000000000000
        a, b = machine.solve()
        cost = 3*a + b
        running_cost += cost
    return running_cost
    
if __name__ == '__main__':
    data = readDataFile()
    result = d13p2(data)
    print(result)
