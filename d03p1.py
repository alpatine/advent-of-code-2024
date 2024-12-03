import re
from math import prod


def readDataFile() -> str:
    with open('d03data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[str]:
    return re.findall('mul\\(\\d{1,3},\\d{1,3}\\)', data)

def evaluate_mul_statement(statement):
    return prod(map(int, re.findall('\d{1,3}', statement)))

def d03p1(data: str) -> int:
    mulStatements = parseData(data)

    running_total = 0
    for mulStatement in mulStatements:
        running_total += evaluate_mul_statement(mulStatement)

    return running_total

if __name__ == '__main__':
    data = readDataFile()
    result = d03p1(data)
    print(result)