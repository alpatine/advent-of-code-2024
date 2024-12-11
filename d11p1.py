def readDataFile() -> str:
    with open('d11data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[str]:
    return list(data.split())

def transform_stones(stones: list[int], cache = {}):
    output = []
    for stone in stones:
        stone_int = int(stone)
        if stone in cache:
            output += cache[stone]
        elif stone_int == 0:
            output.append('1')
        elif len(stone) % 2 == 0:
            left = str(int(stone[:len(stone)//2]))
            right = str(int(stone[len(stone)//2:]))
            cache[stone] = [left, right]
            output.append(left)
            output.append(right)
        else:
            output.append(str(stone_int * 2024))
    return output

def d11p1(data: str, blinks: int) -> int:
    stones = parseData(data)

    for _ in range(blinks):
        stones = transform_stones(stones)

    return len(stones)
    
if __name__ == '__main__':
    data = readDataFile()
    result = d11p1(data, 25)
    print(result)
