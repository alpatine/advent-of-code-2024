import re
from math import prod


def readDataFile() -> str:
    with open('d03data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[str]:
    return re.findall('do\\(\\)|don\'t\\(\\)|mul\\(\\d{1,3},\\d{1,3}\\)', data)

def evaluate_mul_statement(statement):
    return prod(map(int, re.findall('\d{1,3}', statement)))

def d03p2(data: str) -> int:
    running_total = 0
    mul_enabled = True
    statements = parseData(data)
    for statement in statements:
        match statement:
            case 'do()':
                mul_enabled = True
            case 'don\'t()':
                mul_enabled = False
            case _:
                if mul_enabled:
                    running_total += evaluate_mul_statement(statement)

    return running_total

if __name__ == '__main__':
    data = readDataFile()
    result = d03p2(data)
    print(result)