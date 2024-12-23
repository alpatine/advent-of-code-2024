from collections import defaultdict


def readDataFile() -> str:
    with open('d23data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[tuple[str, str]]:
    return [line.split('-') for line in data.splitlines()]

def normalise_connections(connections: list[tuple[str, str]]) -> list[tuple[str, str]]:
    output = []
    for left, right in connections:
        if left < right: output.append((left, right))
        else: output.append((right, left))

    return output

def d23p1(data: str) -> int:
    connections = parseData(data)
    connections = normalise_connections(connections)
    connections.sort()

    graph = defaultdict(set)
    loops = []

    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

        for c in graph[a] & graph[b]:
            if 't' in [a[0], b[0], c[0]]:
                loop = ','.join([a, b, c])
                loops.append(loop)
    
    return len(loops)

if __name__ == '__main__':
    data = readDataFile()
    result = d23p1(data)
    print(result)