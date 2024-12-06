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

def parse_rules(data: list[str]) -> list[tuple[int,int]]:
    rules = []
    for line in data:
        rules.append(tuple(line.split('|')))
    return rules

def parse_updates(data: list[str]) -> list[list[int]]:
    updates = []
    for line in data:
        updates.append(line.split(','))
    return updates
    
def parseData(data: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    blocks = split_data_into_blocks(data)
    rules = parse_rules(blocks[0])
    updates = parse_updates(blocks[1])
    return rules, updates

def check_update(update, rules):
    for pair in pairwise(update):
        page_rules = [rule for rule in rules if rule[0] == pair[0] and rule[1] == pair[1]]
        if len(page_rules) == 0: return False
    return True

def d05p1(data: str) -> int:
    rules, updates = parseData(data)

    middle_page_sum = 0
    for update in updates:
        relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
        if check_update(update, relevant_rules):
            middle_page = update[len(update) // 2]
            middle_page_sum += int(middle_page)
    
    return middle_page_sum

if __name__ == '__main__':
    data = readDataFile()
    result = d05p1(data)
    print(result)
