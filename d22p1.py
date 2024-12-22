from collections import Counter, defaultdict
import sys

def readDataFile() -> str:
    with open('d22data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [int(num) for num in data.splitlines()]

def calculate_secret_number(start: int, steps: int) -> int:
    n = start
    
    for _ in range(steps):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216

    return n

def d22p1(data: str, steps: int) -> str:
    initial_numbers = parseData(data)

    secrets = []

    for num in initial_numbers:
        secret_number = calculate_secret_number(num, steps)
        secrets.append(secret_number)
    
    return sum(secrets)

if __name__ == '__main__':
    data = '''1
10
100
2024'''
    result = d22p1(data, 2000)
    print(result)
    
    data = readDataFile()
    result = d22p1(data, 2000)
    print(result)
