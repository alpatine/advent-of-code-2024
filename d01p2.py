from collections import Counter


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

def d01p2(data: str) -> int:
    leftList, rightList = parseData(data)
    rightCounter = Counter(rightList)

    similarityScoreTotal = 0
    for number in leftList:
        similarityScore = number * rightCounter[number]
        similarityScoreTotal += similarityScore

    return similarityScoreTotal

if __name__ == '__main__':
    data = readDataFile()
    result = d01p2(data)
    print(result)
