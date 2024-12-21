from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, pairwise, permutations
import sys

def readDataFile() -> str:
    with open('d21data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [line for line in data.splitlines()]

def calc_door_paths(start: str, end: str) -> list[str]:
    door_code_locations = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '1': (2, 0), '2': (2, 1), '3': (2, 2),
                         '0': (3, 1), 'A': (3, 2),
    }

    moves_list = []
    sr, sc = door_code_locations[start]
    er, ec = door_code_locations[end]
    dr, dc = er - sr, ec - sc
    if dr < 0: v_move = '^'
    if dr > 0: v_move = 'v'
    if dr == 0: v_move = ''
    if dc < 0: h_move = '<'
    if dc > 0: h_move = '>'
    if dc == 0: h_move = ''

    # Veritcal first option
    if dr != 0 and not (sc == 0 and er == 3):
        moves_list.append(v_move * abs(dr) + h_move * abs(dc) + 'A')

    # Horizontal first option
    if dc != 0 and not (sr == 3 and ec == 0):
        moves_list.append(h_move * abs(dc) + v_move * abs(dr) + 'A')

    if (dr, dc) == (0, 0): moves_list.append('A')

    return moves_list

def calc_dpad_path_length(start: str, end: str, robot_count: int, memo = {}) -> list[int]:
    key = (start, end, robot_count)
    if key in memo: return memo[key]

    dpad_locations = {
                     '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    }
    path_list = []
    sr, sc = dpad_locations[start]
    er, ec = dpad_locations[end]
    dr, dc = er - sr, ec - sc

    if dr < 0: v_move = '^'
    if dr > 0: v_move = 'v'
    if dr == 0: v_move = ''
    if dc < 0: h_move = '<'
    if dc > 0: h_move = '>'
    if dc == 0: h_move = ''

    # Veritcal first option
    if dr != 0 and not (sc == 0 and er == 0):
        path_list.append(v_move * abs(dr) + h_move * abs(dc) + 'A')

    # Horizontal first option
    if dc != 0 and not (sr == 0 and ec == 0):
        path_list.append(h_move * abs(dc) + v_move * abs(dr) + 'A')

    if (dr, dc) == (0, 0): path_list.append('A')

    if robot_count == 1:
        ret = min(list(map(len,path_list)))
        memo[key] = ret
        return ret

    # More robots to push this through
    path_lengths = []
    for path in path_list:
        path_length = 0
        for a, b in pairwise('A' + path):
            step_length = calc_dpad_path_length(a, b, robot_count-1)
            path_length += step_length
        path_lengths.append(path_length)
    ret = min(path_lengths)
    memo[key] = ret
    return ret

def calculate_door_paths(door_code: str, robot_count: int) -> list[str]:
    door_code_path_length = 0
    for a, b in pairwise('A' + door_code):
        path_list = calc_door_paths(a, b)
        path_lengths = []
        for path in path_list:
            path_length = 0
            for a, b in pairwise('A' + path):
                step_length = calc_dpad_path_length(a, b, robot_count)
                path_length += step_length
            path_lengths.append(path_length)
        door_code_path_length += min(path_lengths)
    return door_code_path_length

def d21p2(data: str, robot_count: int) -> str:
    door_codes = parseData(data)

    total_complexity = 0
    for door_code in door_codes:
        shortest_length = calculate_door_paths(door_code, robot_count)
        complexity = int(door_code[:3]) * shortest_length
        total_complexity += complexity

    return total_complexity

if __name__ == '__main__':
    data = '''029A
980A
179A
456A
379A'''
    result = d21p2(data, 2)
    print(result)
    
    data = readDataFile()
    result = d21p2(data, 25)
    print(result)