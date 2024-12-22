def readDataFile() -> str:
    with open('d19data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> tuple[list[str], list[str]]:
    towels, designs = data.split('\n\n')
    towels = list(map(str.strip, towels.split(',')))
    designs = designs.splitlines()
    return towels, designs

def if_possible(design: str, towels: list[str]) -> int:
    possible = [0] * (len(design)+1)
    possible[0] = 1

    for pos in range(len(design) + 1):
        ways_to_here = possible[pos]
        if ways_to_here == 0: continue
        match = design[pos:]
        for towel in towels:
            if match.startswith(towel):
                possible[pos + len(towel)] += ways_to_here
    
    return possible[len(design)]

def d19p2(data: str) -> str:
    towels, designs = parseData(data)
    possible_count = 0
    for design in designs:
        possible_count += if_possible(design, towels)
    return possible_count
    
if __name__ == '__main__':
    data = readDataFile()
    result = d19p2(data)
    print(result)
