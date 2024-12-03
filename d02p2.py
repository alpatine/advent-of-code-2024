from itertools import pairwise


def readDataFile() -> str:
    with open('d02data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> list[list[int]]:
    reports = []
    for line in data.splitlines():
        reports.append(list(map(int,line.split())))
    return reports

def signum(a) -> int:
    if a > 0: return 1
    elif a < 0: return -1
    else: return 0

def check_safety(report: list[int]) -> bool:
    sign = signum(report[-1] - report[0])
    for left,right in pairwise(report):
        if not 1 <= sign * (right - left) <= 3:
            return False
    return True
        
def check_safety_with_dampener(report: list[int]) -> bool:
    if (check_safety(report)): return True
    for pos in range(len(report)):
        shorter_report = report[:pos] + report[pos+1:]
        if check_safety(shorter_report): return True
    
def d02p2(data: str) -> int:
    reports = parseData(data)
    safe_reports_count = 0
    for report in reports:
        if check_safety_with_dampener(report): safe_reports_count += 1

    return safe_reports_count

if __name__ == '__main__':
    data = readDataFile()
    result = d02p2(data)
    print(result)
