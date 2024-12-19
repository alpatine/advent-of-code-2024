class Computer:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.code = ''
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

def d17p1(data: str) -> str:
    computer = parseData(data)
    computer.run_code()
    return ','.join(map(str,computer.output))
    
if __name__ == '__main__':
    data = readDataFile()
    result = d17p1(data)
    print(result)
