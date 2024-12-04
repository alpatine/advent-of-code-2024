def readDataFile() -> str:
    with open('d04data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def d04p2(data: str) -> int:
    grid = parseData(data)
    rows = len(grid)
    cols = len(grid[0])

    xmas_count = 0
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] == "A":
                ul = grid[row-1][col-1]
                ur = grid[row-1][col+1]
                dl = grid[row+1][col-1]
                dr = grid[row+1][col+1]
                if ((ul in 'MS' and dr in 'MS' and ul != dr)
                        and (ur in 'MS' and dl in 'MS' and ur != dl)):
                    xmas_count += 1

    return xmas_count

if __name__ == '__main__':
    data = readDataFile()
    result = d04p2(data)
    print(result)