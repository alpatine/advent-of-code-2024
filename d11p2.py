def readDataFile() -> str:
    with open('d11data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[str]:
    return list(data.split())

def count_stone(stone: str, blinks: int, memo = {}) -> str:
    if blinks == 0: return 1

    total = 0
    if blinks >= 3 and stone in ['1', '2', '3']:
        key = (stone, blinks)
        if key in memo:
            total += memo[key]
        else:
            match stone:
                case '1': d = [(2, '2'), (1, '0'), (1, '4')]
                case '2': d = [(2, '4'), (1, '0'), (1, '8')]
                case '3': d = [(1, '6'), (1, '0'), (1, '7'), (1, '2')]
                case '4': d = [(1, '8'), (1, '0'), (1, '9'), (1, '6')]
            for m, s in d:
                total += m * count_stone(s, blinks-3)
            memo[key] = total
    elif blinks >= 5 and stone in ['5', '6', '7', '9']:
        key = (stone, blinks)
        if key in memo:
            total += memo[key]
        else:
            match stone:
                case '5': d = [(2, '0'), (2, '2'), (1, '4'), (3, '8')]
                case '6': d = [(1, '2'), (2, '4'), (2, '5'), (1, '7'), (1, '9'), (1, '6')]
                case '7': d = [(1, '0'), (2, '2'), (1, '3'), (2, '6'), (1, '7'), (1, '8')]
                case '9': d = [(1, '3'), (2, '6'), (2, '8'), (1, '9'), (1, '1'), (1, '4')]
            for m, s in d:
                total += m * count_stone(s, blinks-5)
            memo[key] = total
    elif blinks >= 5 and stone == '8':
        key = (stone, blinks)
        if key in memo:
            total += memo[key]
        else:
            match stone:
                case '8': d = [(2, '2'), (1, '3'), (1, '6'), (2, '7')]
            for m, s in d:
                total += m * count_stone(s, blinks-5)
            total += count_stone('8', blinks-4)
            memo[key] = total
    elif blinks >= 4 and stone == '0':
        next_stones = '2024'
        for s in next_stones:
            total += count_stone(s, blinks-4)
    else:
        if stone == '0':
            total += count_stone('1', blinks-1)
        elif len(stone) % 2 == 0:
            left_total = count_stone(str(int(stone[:len(stone)//2])), blinks-1)
            right_total = count_stone(str(int(stone[len(stone)//2:])), blinks-1)
            total += left_total + right_total
        else:
            total += count_stone(str(int(stone)*2024), blinks-1)
    
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
