from collections import defaultdict
import re

class Wire:
    def __init__(self):
        self.name = ''
        self.value = None
        self.source_gate: Gate = None

    def __repr__(self):
        return f'name={self.name} value={self.value}'
    
    def get_value(self) -> int:
        if self.value is None:
            self.value = self.source_gate.get_value()
        return self.value

class Gate:
    def __init__(self):
        self.type = ''
        self.leftInput: Wire = None
        self.rightInput: Wire = None
    
    def __repr__(self):
        return f'{self.leftInput} {self.type} {self.rightInput} -> {self.output}'
    
    def get_value(self) -> int:
        l = self.leftInput.get_value()
        r = self.rightInput.get_value()
        
        match self.type:
            case 'AND': return l & r
            case 'OR': return l | r
            case 'XOR': return l ^ r
            

def readDataFile() -> str:
    with open('d24data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> dict[str, Wire]:
    wires: dict[str, Wire] = defaultdict(Wire)
    
    initial_vals, gates = data.split('\n\n')
    for line in initial_vals.splitlines():
        name, val = line.split(':')
        val = val.strip()
        wire = wires[name]
        wire.name = name
        wire.value = int(val)
    
    for line in gates.splitlines():
        parts = re.match(r'(...) (AND|OR|XOR) (...) -> (...)', line)
        left_wire_name = parts[1]
        gate_type = parts[2]
        right_wire_name = parts[3]
        output_wire_name = parts[4]
        
        gate = Gate()
        left_wire = wires[left_wire_name]
        left_wire.name = left_wire_name
        gate.leftInput = left_wire

        gate.type = gate_type

        right_wire = wires[right_wire_name]
        right_wire.name = right_wire_name
        gate.rightInput = right_wire

        output_wire = wires[output_wire_name]
        output_wire.name = output_wire_name
        output_wire.source_gate = gate

    return wires

def d24p1(data: str) -> int:
    wires = parseData(data)
    output_wires = [wire for wire in wires.keys() if wire.startswith('z')]
    output_wires.sort(reverse=True)
    
    output_value = 0
    for wire_name in output_wires:
        output_value <<= 1
        wire = wires[wire_name]
        output_value += wire.get_value()

    return output_value

if __name__ == '__main__':
#     data = '''x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02'''
#     result = d24p1(data)
#     print(result)

#     data = '''x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj'''
#     result = d24p1(data)
#     print(result)
    
    data = readDataFile()
    result = d24p1(data)
    print(result)