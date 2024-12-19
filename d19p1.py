def readDataFile() -> str:
    with open('d19data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> tuple[list[str], list[str]]:
    towels, designs = data.split('\n\n')
    towels = list(map(str.strip, towels.split(',')))
    designs = designs.splitlines()
    return towels, designs

def if_possible(design: str, towels: list[str]) -> bool:
    possible = [False] * (len(design)+1)
    possible[0] = True

    for pos in range(len(design) + 1):
        if possible[pos] == False: continue
        match = design[pos:]
        for towel in towels:
            if match.startswith(towel):
                possible[pos + len(towel)] = True
    
    return possible[len(design)]

def d19p1(data: str) -> str:
    towels, designs = parseData(data)
    possible_count = 0
    for design in designs:
        if if_possible(design, towels):
            possible_count += 1
    return possible_count
    
if __name__ == '__main__':
    data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
    data = readDataFile()
    result = d19p1(data)
    print(result)
