from collections import defaultdict


def readDataFile() -> str:
    with open('d23data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[tuple[str, str]]:
    return [line.split('-') for line in data.splitlines()]

def build_graph(connections: list[str]) -> dict[str, set[str]]:
    graph = defaultdict(set)
    for left, right in connections:
        graph[left].add(right)
        graph[right].add(left)
    return graph

def find_largest_mesh(graph: dict[str,set[str]], included: set[str], explore_nodes: set[str], finished_nodes: set[str]) -> list[set[str]]:
    largest_mesh_found = set()
    if len(explore_nodes) == 0 and len(finished_nodes) == 0: return included
    for e in list(explore_nodes):
        neighbours = graph[e]
        mesh_found = find_largest_mesh(graph, included | {e}, explore_nodes & neighbours, finished_nodes & neighbours)
        if len(mesh_found) > len(largest_mesh_found):
            largest_mesh_found = mesh_found
        explore_nodes -= {e}
        finished_nodes |= {e}
    return largest_mesh_found

def calculate_password(mesh: set[str]) -> str:
    mesh_elements = list(mesh)
    mesh_elements.sort()
    password = ','.join(mesh_elements)
    return password

def d23p2(data: str) -> int:
    connections = parseData(data)
    graph = build_graph(connections)
    largest_mesh = find_largest_mesh(graph, set(), set(graph.keys()), set())
    password = calculate_password(largest_mesh)
    return password

if __name__ == '__main__':
    data = readDataFile()
    result = d23p2(data)
    print(result)