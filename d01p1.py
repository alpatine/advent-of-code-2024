def readDataFile() -> str:
    with open('d01data.txt') as dataFile:
        return dataFile.read()
    
def parseData(data: str) -> tuple[list[int],list[int]]:
    leftList = []
    rightList = []
    for line in data.splitlines():
        leftStr,rightStr = line.split()
        leftList.append(int(leftStr))
        rightList.append(int(rightStr))
    return leftList, rightList

def d01p1(data: str) -> int:
    leftList, rightList = parseData(data)
    leftList.sort()
    rightList.sort()

    distanceSum = 0
    for pos in range(0, len(leftList)):
        distance = abs(leftList[pos] - rightList[pos])
        distanceSum += distance

    return distanceSum

if __name__ == '__main__':
    data = readDataFile()
    result = d01p1(data)
    print(result)
