from collections import Counter, defaultdict
import sys

class DoorCodeWalker:
    door_code_locations = {
            'A': (3, 2),
            '0': (3, 1),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
    }
    
    def __init__(self):
        self.r = 3
        self.c = 2

    def get_code_moves(self, code: str) -> list[str]:
        moves_list = ['']
        for c in code:
            digit_moves = self.get_digit_moves(c)
            new_moves_list = [b+dm for b in moves_list for dm in digit_moves]
            moves_list = new_moves_list
        return moves_list
    
    def get_digit_moves(self, target: str) -> list[str]:
        moves_list = []
        tr, tc = self.door_code_locations[target]
        dr, dc = tr - self.r, tc - self.c
        if dr < 0: v_move = '^'
        if dr > 0: v_move = 'v'
        if dr == 0: v_move = ''
        if dc < 0: h_move = '<'
        if dc > 0: h_move = '>'
        if dc == 0: h_move = ''

        # Veritcal first option
        if dr != 0 and not (self.c == 0 and tr == 3):
            moves_list.append(v_move * abs(dr) + h_move * abs(dc) + 'A')

        # Horizontal first option
        if dc != 0 and not (self.r == 3 and tc == 0):
            moves_list.append(h_move * abs(dc) + v_move * abs(dr) + 'A')

        if (dr, dc) == (0, 0): moves_list.append('A')

        self.r, self.c = tr, tc

        return moves_list

class DPadCodeWalker:
    dpad_locations = {
        '^': (0, 1),
        'A': (0, 2),
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2),
    }

    def __init__(self):
        self.r = 0
        self.c = 2
    
    def get_code_moves(self, code: str) -> list[str]:
        moves_list = ['']
        for c in code:
            digit_moves = self.get_digit_moves(c)
            new_moves_list = [b+dm for b in moves_list for dm in digit_moves]
            moves_list = new_moves_list
        return moves_list
    
    def get_digit_moves(self, target: str) -> list[str]:
        moves_list = []
        tr, tc = self.dpad_locations[target]
        dr, dc = tr - self.r, tc - self.c

        if dr < 0: v_move = '^'
        if dr > 0: v_move = 'v'
        if dr == 0: v_move = ''
        if dc < 0: h_move = '<'
        if dc > 0: h_move = '>'
        if dc == 0: h_move = ''

        # Veritcal first option
        if dr != 0 and not (self.c == 0 and tr == 0):
            moves_list.append(v_move * abs(dr) + h_move * abs(dc) + 'A')

        # Horizontal first option
        if dc != 0 and not (self.r == 0 and tc == 0):
            moves_list.append(h_move * abs(dc) + v_move * abs(dr) + 'A')

        if (dr, dc) == (0, 0): moves_list.append('A')

        self.r, self.c = tr, tc

        return moves_list

def readDataFile() -> str:
    with open('d21data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[str]]:
    return [line for line in data.splitlines()]

def d21p1(data: str) -> str:
    door_codes = parseData(data)
    total_complexity = 0
    for door_code in door_codes:

        door_walker = DoorCodeWalker()
        dpad1_walker = DPadCodeWalker()
        dpad2_walker = DPadCodeWalker()

        dpad1_codes = door_walker.get_code_moves(door_code)

        dpad2_codes = []
        for dpad1_code in dpad1_codes:
            dpad2_codes += dpad1_walker.get_code_moves(dpad1_code)

        dpad3_codes = []
        for dpad2_code in dpad2_codes:
            dpad3_codes += dpad2_walker.get_code_moves(dpad2_code)

        shortest_len = sys.maxsize
        for code in dpad3_codes:
            l = len(code)
            if l < shortest_len:
                shortest_len = l

        # dpad1_moves = get_door_code_moves(door_code)
        # dpad2_moves = get_dpad_moves(dpad1_moves)
        # dpad3_moves = get_dpad_moves(dpad2_moves)
        complexity = int(door_code[:3]) * shortest_len
        total_complexity += complexity

    return total_complexity

if __name__ == '__main__':
    data = '''029A
980A
179A
456A
379A'''
    result = d21p1(data)
    print(result)
    
    data = readDataFile()
    result = d21p1(data)
    print(result)

    #258330 is too high