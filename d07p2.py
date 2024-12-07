def readDataFile() -> str:
    with open('d07data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    equations = []
    for line in data.splitlines():
        target, value_list = line.split(':')
        values = value_list.split()
        equations.append((int(target), list(map(int, values))))
    return equations

def can_calibrate(target: int, acc: int, pos: int, values: list[int]) -> bool:
    if acc > target: return False
    if pos == len(values): return target == acc
    
    # Check multiply
    new_acc = acc * values[pos]
    if can_calibrate(target, new_acc, pos + 1, values): return True

    # Check add
    new_acc = acc + values[pos]
    if can_calibrate(target, new_acc, pos + 1, values): return True

    # Check concat
    new_acc = int(str(acc) + str(values[pos]))
    if can_calibrate(target, new_acc, pos + 1, values): return True

    return False

def d07p2(data: str) -> int:
    equations = parseData(data)
    value_sum = 0
    for equation in equations:
        if can_calibrate(equation[0], equation[1][0], 1, equation[1]):
            value_sum += equation[0]

    return value_sum
    
if __name__ == '__main__':
    data = readDataFile()
    result = d07p2(data)
    print(result)
