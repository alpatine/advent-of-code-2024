from itertools import pairwise


def readDataFile() -> str:
    with open('d02data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[list[str]]:
    reports = []
    for line in data.splitlines():
        reports.append(list(map(int,line.split())))
    return reports

def signum(a: int) -> int:
    if a > 0: return 1
    elif a < 0: return -1
    else: return 0

def check_safety(report: list[int]) -> bool:
    sign = signum(report[-1] - report[0])
    for left,right in pairwise(report):
        if not 1 <= sign * (right - left) <= 3:
            return False
    return True

def d02p1(data: str) -> int:
    reports = parseData(data)
    safe_report_count = 0
    for report in reports:
        if check_safety(report): safe_report_count += 1

    return safe_report_count

if __name__ == '__main__':
    data = readDataFile()
    result = d02p1(data)
    print(result)
