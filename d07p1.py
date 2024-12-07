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

def can_calibrate(target: int, values: list[int], memo: dict[tuple[int, int], bool]) -> int:
    if len(values) == 1: return values[0] == target
    
    # Check multiply
    product = values[0] * values[1]
    new_values = [product] + values[2:]
    if can_calibrate(target, new_values, memo): return True

    # Check add
    sum = values[0] + values[1]
    new_values = [sum] + values[2:]
    if can_calibrate(target, new_values, memo): return True

    return False

def can_calibrate2(target: int, acc: int, pos:int, values: list[int]) -> bool:
    if acc > target: return False
    if pos == len(values): return target == acc
    
    # Check multiply
    new_acc = acc * values[pos]
    if can_calibrate2(target, new_acc, pos + 1, values): return True

    # Check add
    new_acc = acc + values[pos]
    if can_calibrate2(target, new_acc, pos + 1, values): return True

    return False

def d07p1(data: str) -> int:
    equations = parseData(data)
    value_sum = 0
    for equation in equations:
        if can_calibrate2(equation[0], equation[1][0], 1, equation[1]):
            value_sum += equation[0]

    return value_sum
    
if __name__ == '__main__':
    data = readDataFile()
    result = d07p1(data)
    print(result)
