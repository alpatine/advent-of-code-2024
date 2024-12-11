def readDataFile() -> str:
    with open('d11data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[int]:
    return list(map(int, data.split()))

def count_stone(stone: int, blinks: int, memo = {}) -> int:
    if blinks == 0: return 1
    
    key = (stone, blinks)
    if key in memo: return memo[key]

    total = 0
    if stone == 0:
        total += count_stone(1, blinks-1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        left_total = count_stone(int(stone_str[:len(stone_str)//2]), blinks-1)
        right_total = count_stone(int(stone_str[len(stone_str)//2:]), blinks-1)
        total += left_total + right_total
    else:
        total += count_stone(stone*2024, blinks-1)
    
    memo[key] = total
    return total

def d11p2(data: str, blinks: int) -> int:
    stones = parseData(data)
    total = 0
    for stone in stones:
        total += count_stone(stone, blinks)
    return total
    
if __name__ == '__main__':
    data = readDataFile()
    result = d11p2(data, 75)
    print(result)
