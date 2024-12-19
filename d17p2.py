class Computer:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.code = []
        self.P = 0
        self.output = []

    def __repr__(self):
        return f'A={self.A} B={self.B} C={self.C} P={self.P}'
    
    def combo(self, c: int) -> int:
        if 0 <= c <= 3: return c
        match c:
            case 4: return self.A
            case 5: return self.B
            case 6: return self.C
    
    def run_code(self) -> None:
        program_length = len(self.code)
        while self.P < program_length:
            opcode, operand = self.code[self.P:self.P+2]
            match opcode:
                case 0: self.adv(operand)
                case 1: self.bxl(operand)
                case 2: self.bst(operand)
                case 3: self.jnz(operand)
                case 4: self.bxc(operand)
                case 5: self.out(operand)
                case 6: self.bdv(operand)
                case 7: self.cdv(operand)

    def adv(self, o: int) -> None:
        self.A = self.A // (2**self.combo(o))
        self.P += 2

    def bxl(self, o: int) -> None:
        self.B = self.B ^ o
        self.P += 2
    
    def bst(self, o: int) -> None:
        self.B = self.combo(o) % 8
        self.P += 2

    def jnz(self, o: int) -> None:
        if self.A != 0: self.P = o
        else: self.P += 2

    def bxc(self, o: int) -> None:
        self.B = self.B ^ self.C
        self.P += 2
    
    def out(self, o: int) -> None:
        self.output.append(self.combo(o) % 8)
        self.P += 2
    
    def bdv(self, o: int) -> None:
        self.B = self.A // (2**self.combo(o))
        self.P += 2
    
    def cdv(self, o: int) -> None:
        self.C = self.A // (2**self.combo(o))
        self.P += 2


def readDataFile() -> str:
    with open('d17data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> Computer:
    computer = Computer()
    registers, code = data.split('\n\n')
    computer.A, computer.B, computer.C = map(int, [r.split(':')[1].strip() for r in registers.splitlines()])
    computer.code = list(map(int, code.split(':')[1].strip().split(',')))
    return computer
    
def compute(a: int, b: int, c: int, code: list[int]) -> int:
    computer = Computer()
    computer.A, computer.B, computer.C, computer.code = a, b, c, code
    computer.run_code()
    return computer.output

def find_input(b: int, c: int, code: str, target: str) -> int:
    required_octets = len(target)
    trial_values = [0] * len(target)

    pos = 0
    while 0 <= pos < required_octets:
        # check if we've overflowed any positions
        if trial_values[pos] == 8:
            for _ in range(pos, len(trial_values)):
                trial_values[_] = 0
            pos -= 1
            trial_values[pos] += 1
            continue

        # run the program
        test_value = int(''.join(map(str,trial_values)), 8)
        output = compute(test_value, b, c, code)

        # check if we are on track
        if target[-1-pos:] == output[-1-pos:]: pos += 1
        else: trial_values[pos] += 1
    
    return test_value

def d17p2(data: str) -> str:
    computer = parseData(data)
    (b, c, code) = computer.B, computer.C, computer.code
    result = find_input(b, c, code, code)
    return result
    
if __name__ == '__main__':
    data = readDataFile()
    result = d17p2(data)
    print(result)
