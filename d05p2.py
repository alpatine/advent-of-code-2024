from collections import defaultdict
from functools import cmp_to_key
from itertools import pairwise


def readDataFile() -> str:
    with open('d05data.txt') as dataFile:
        return dataFile.read()

def split_data_into_blocks(raw_data: str) -> list[list[str]]:
    blocks = [[]]
    current_block = blocks[0]

    for line in raw_data.splitlines():
        if line != '':
            current_block.append(line)
        else: 
            current_block = []
            blocks.append(current_block)

    return blocks

def parse_rules(data: list[str]) -> dict[int,int]:
    rules = defaultdict(list)
    for line in data:
        key, value = line.split('|')
        rules[int(key)].append(int(value))
    return rules

def parse_updates(data: list[str]) -> list[list[int]]:
    updates = []
    for line in data:
        updates.append(list(map(int,line.split(','))))
    return updates
    
def parseData(data: str) -> tuple[dict[int, int], list[list[int]]]:
    blocks = split_data_into_blocks(data)
    rules = parse_rules(blocks[0])
    updates = parse_updates(blocks[1])
    return rules, updates

def check_update(update: list[int], rules: dict[int, int]) -> bool:
    for pair in pairwise(update):
        later_pages = rules[pair[0]]
        if pair[1] not in later_pages: return False
    return True

def sort_update(update: list[int], rules: list[tuple[int,int]]) -> list[int]:
    def cmp(a, b):
        if b in rules[a]: return -1
        else: return 1
    sorted_update = list(sorted(update, key=cmp_to_key(cmp)))
    return sorted_update

def d05p2(data: str) -> int:
    rules, updates = parseData(data)

    middle_page_sum = 0
    for update in updates:
        if check_update(update, rules) == False:
            sorted_update = sort_update(update, rules)
            middle_page = sorted_update[len(sorted_update) // 2]
            middle_page_sum += int(middle_page)
    return middle_page_sum

if __name__ == '__main__':
    data = readDataFile()
    result = d05p2(data)
    print(result)
