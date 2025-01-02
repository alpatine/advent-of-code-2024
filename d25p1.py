def readDataFile() -> str:
    with open('d25data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> tuple[list[list[int]], list[list[int]]]:
    blocks = data.split('\n\n')

    locks = list()
    keys = list()

    for block in blocks:
        block_lines = block.splitlines()
        block_height = len(block_lines)
        block_width = len(block_lines[0])
        indicator_row = '#' * block_width
        cells = [[c for c in row] for row in block_lines]
        if block_lines[0] == indicator_row:
            # This is a lock
            lock = []
            for c in range(block_width):
                for r in range(block_height):
                    if cells[r][c] == '.':
                        lock.append(r-1)
                        break
            locks.append(lock)
        else:
            # This is a key
            key = []
            for c in range(block_width):
                for r in range(block_height):
                    if cells[block_height - r - 1][c] == '.':
                        key.append(r-1)
                        break
            keys.append(key)
    
    return locks, keys

def count_fits(locks: list[list[int]], keys: list[list[int]]) -> tuple[int, int]:
    fits = 0
    for lock in locks:
        for key in keys:
            for pos in range(len(lock)):
                if lock[pos] + key[pos] > 5:
                    break
            else:
                fits += 1
    return fits


def d25p1(data: str) -> int:
    locks, keys = parseData(data)
    fits = count_fits(locks, keys)
    return fits
    
if __name__ == '__main__':    
    data = readDataFile()
    result = d25p1(data)
    print(result)