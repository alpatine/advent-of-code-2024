def readDataFile() -> str:
    with open('d04data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[list[str]]:
    return [[char for char in line] for line in data.splitlines()]

def find_xmas(grid: list[list[str]],
              row: int,
              col: int,
              row_direction: int,
              col_direction: int
              ) -> int:
    word = "XMAS"
    for step in range(len(word)):
        if grid[row + row_direction * step][col + col_direction * step] != word[step]:
            return 0
    return 1

def d04p1(data: str) -> int:
    grid = parseData(data)
    rows = len(grid)
    cols = len(grid[0])

    xmas_count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "X":
                can_go_north = row - 4 >= -1
                can_go_south = row + 4 <= rows
                can_go_east = col + 4 <= cols
                can_go_west = col - 4 >= -1

                if can_go_north:
                    xmas_count += find_xmas(grid, row, col, -1, 0)
                    if can_go_east:
                        xmas_count += find_xmas(grid, row, col, -1, 1)
                    if can_go_west:
                        xmas_count += find_xmas(grid, row, col, -1, -1)
                if can_go_east:
                    xmas_count += find_xmas(grid, row, col, 0, 1)
                if can_go_west:
                    xmas_count += find_xmas(grid, row, col, 0, -1)
                if can_go_south:
                    xmas_count += find_xmas(grid, row, col, 1, 0)
                    if can_go_east:
                        xmas_count += find_xmas(grid, row, col, 1, 1)
                    if can_go_west:
                        xmas_count += find_xmas(grid, row, col, 1, -1)

    return xmas_count

if __name__ == '__main__':
    data = readDataFile()
    result = d04p1(data)
    print(result)