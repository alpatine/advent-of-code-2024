from collections import Counter, defaultdict
from itertools import combinations
import re

class Wire:
    def __init__(self):
        self.name = ''
        self.value = None
        self.initial_value = None
        self.source_gate: Gate = None

    def __repr__(self):
        return f'name={self.name} value={self.value}'
    
    def get_value(self) -> int:
        if self.value is None:
            if self.initial_value is not None:
                self.value = self.initial_value
            else:
                self.value = self.source_gate.get_value()
        return self.value

    def reset(self) -> None:
        self.value = None
        if self.source_gate is not None:
            self.source_gate.reset()

class Gate:
    def __init__(self):
        self.type = ''
        self.leftInput: Wire = None
        self.rightInput: Wire = None
    
    def __repr__(self):
        return f'{self.leftInput} {self.type} {self.rightInput}'
    
    def get_value(self) -> int:
        l = self.leftInput.get_value()
        r = self.rightInput.get_value()
        
        match self.type:
            case 'AND': return l & r
            case 'OR': return l | r
            case 'XOR': return l ^ r
    
    def reset(self) -> None:
        if self.leftInput is not None: self.leftInput.reset()
        if self.rightInput is not None: self.rightInput.reset()
            

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
        wire.initial_value = int(val)
    
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

def calculate_decimals(wires: dict[str, Wire], names_list: list[list[str]]) -> list[int]:
    output_value: list[int] = []
    for name_list in names_list:
        value = 0
        for name in sorted(name_list, reverse=True):
            value <<= 1
            wire = wires[name]
            value += wire.get_value()
        output_value.append(value)
    return output_value

def print_checks(x: int, y: int, z: int) -> None:
    print(f'Input: {format(x, '046b')}')
    print(f'Input: {format(y, '046b')}')
    print(f'Calc:  {format(z, '046b')}')
    print(f'Real:  {format(x+y, '046b')}')
    print(f'Diff:  {format((x+y)^z, '046b')}')

def print_sources(wire: Wire, depth: int = 0) -> None:
    bars = '| ' * depth
    if wire.source_gate is not None:
        print(f'{bars}{wire.name} {wire.source_gate.type}')
        print_sources(wire.source_gate.leftInput, depth + 1)
        print_sources(wire.source_gate.rightInput, depth + 1)
    else:
        print(f'{bars}{wire.name}')

def get_source_wires(wire: Wire) -> set[str]:
    output = {wire.name}
    if wire.source_gate is not None:
        output |= get_source_wires(wire.source_gate.leftInput)
        output |= get_source_wires(wire.source_gate.rightInput)
    return output

def zero_inputs(wires: dict[str, Wire], zero_names: list[str]) -> None:
    for name in wires.keys():
        wires[name].value = None
    for name in zero_names:
        wires[name].value = 0

def set_network(wires: dict[str, Wire], x: int, y: int) -> None:
    for name in wires.keys():
        wires[name].value = None
    x_bits = format(x, '045b')[::-1]
    for pos, bit in enumerate(x_bits):
        wires[f'x{format(pos, '02')}'].value = int(bit)
    
    y_bits = format(y, '045b')[::-1]
    for pos, bit in enumerate(y_bits):
        wires[f'y{format(pos, '02')}'].value = int(bit)

def get_names(wires: dict[str, Wire], prefix: str) -> list[str]:
    names = [name for name in wires.keys() if name.startswith(prefix)]
    names.sort()
    return names

def test_value(
        wires: dict[str, Wire],
        power: int,
        names_list: list[list[str]]
        ) -> set[str]:
    
    bad_wires = set()
    test_x = 2**power-1
    test_y = 2**power-1

    set_network(wires, test_x, test_y)
    x, y, z = calculate_decimals(wires, names_list)
    target_output = test_x + test_y
    error_bits = format(target_output ^ z, 'b')[::-1]

    #for bit_pos in range(max(0, power-2), min(power+3, len(error_bits))):
    if error_bits != '0':
        seen_wires = set()
        for bit_pos, bit in enumerate(error_bits):
#            if power-1 <= bit_pos <= power+2:
            #bit = error_bits[bit_pos]
            zn = 'z' + format(bit_pos, '02')
            sources = get_source_wires(wires[zn])
            if bit == '0':
                seen_wires |= sources
                #bad_wires -= current_good_wires
            if bit == '1':
                bad_wires |= sources - seen_wires
                seen_wires |= sources
            #print()
        #print_sources(wires[zn])
    print_checks(x, y, z)
    print(','.join(list(sorted(bad_wires))))
    return bad_wires

def find_structure_errors(wires: dict[str, Wire], z_pos: int) -> set[str]:
    errors = set()
    # The first gate should be an XOR
    z_name = f'z{format(z_pos, '02')}'
    wire_sxor = wires[z_name]
    
    gate_sxor = wire_sxor.source_gate
    if gate_sxor.type != 'XOR':
        errors.add(z_name)
    
    if {'XOR', 'OR'} != {gate_sxor.leftInput.source_gate.type, gate_sxor.rightInput.source_gate.type}:
        errors.add(z_name)

    if gate_sxor.leftInput.source_gate.type == 'XOR':
        wire_sixor = gate_sxor.leftInput
        wire_cor = gate_sxor.rightInput
    elif gate_sxor.rightInput.source_gate.type == 'XOR':
        wire_sixor = gate_sxor.rightInput
        wire_cor = gate_sxor.leftInput
    else:
        # problems
        errors.add(z_name)

    gate_sixor = wire_sixor.source_gate 
    sixor_x_name = f'x{format(z_pos, '02')}'
    sixor_y_name = f'y{format(z_pos, '02')}'
    # Gate sixor should be conmected to intputs
    if {sixor_x_name, sixor_y_name} != {gate_sixor.leftInput.name, gate_sixor.rightInput.name}:
        # problems
        errors.add(wire_sixor)

    gate_cor = wire_cor.source_gate
    if {'AND'} != {gate_cor.leftInput.source_gate.type, gate_cor.rightInput.source_gate.type}:
        errors.add(wire_cor)
    
def get_inputs(wire: Wire) -> set[Wire]:
    output = set()
    if wire.name[0] in {'x', 'y'}:
        return {wire}
    else:
        output |= get_inputs(wire.source_gate.leftInput)
        output |= get_inputs(wire.source_gate.rightInput)
    
    return output

def swap_wires(wires: dict[str, Wire], w1_name: str, w2_name: str) -> None:
    w1 = wires[w1_name]
    w2 = wires[w2_name]
    w1.source_gate, w2.source_gate = w2.source_gate, w1.source_gate

def check_adder_xor_xor_inputs(wires: dict[str, Wire], z_names) -> set[str]:
    errors = set()
    for z_names in z_names:
        z_wire = wires[z_names]
        z_num = z_names[1:]

        # find the first xor gate
        z_gate = z_wire.source_gate
        if z_gate.type != 'XOR':
            errors.add(z_names)
            return errors

        # check that it has xor and or as inputs
        if {z_gate.leftInput.source_gate.type, z_gate.rightInput.source_gate.type} != {'XOR', 'OR'}:
            errors.add(z_gate.leftInput.name)
            errors.add(z_gate.rightInput.name)
            return errors

        # find the second xor gate (input xor gate)
        if z_gate.leftInput.source_gate.type == 'XOR':
            xor_input_wire = z_gate.leftInput
        else: xor_input_wire = z_gate.rightInput
        xor_input_gate = xor_input_wire.source_gate

        # check that we now have an x and y input, with the same number as the z output
        required_x_name = f'x{z_num}'
        required_y_name = f'y{z_num}'
        if {xor_input_gate.leftInput.name, xor_input_gate.rightInput.name} != {required_x_name, required_y_name}:
            pass

def check_input_and(wire: Wire) -> tuple[bool, set[str]]:
    if wire.source_gate is None: return True, None
    gate = wire.source_gate
    if gate.type != 'AND': return False, {wire.name}

    if {'x', 'y'} != {gate.leftInput.name[0], gate.rightInput.name[0]}:
        return False, {wire.name}
    
    return True, {}

def check_input_xor(wire: Wire) -> tuple[bool, set[str]]:
    if wire.source_gate is None: return True, None
    gate = wire.source_gate
    if gate.type != 'XOR': return False, {wire.name}

    if {'x', 'y'} != {gate.leftInput.name[0], gate.rightInput.name[0]}:
        return False, {wire.name}
    
    return True, {}

def check_carry_and(wire: Wire) -> tuple[bool, set[str]]:
    if wire.source_gate is None: return True, {}
    gate = wire.source_gate
    if gate.type != 'AND': return False, {wire.name}

    errors = set()
    if gate.leftInput.name != 'mtk' and gate.leftInput.source_gate is not None and gate.leftInput.source_gate.type not in ('XOR', 'OR'):
        errors.add(gate.leftInput.name)
    
    if gate.rightInput.name != 'mtk' and gate.rightInput.source_gate is not None and gate.rightInput.source_gate.type not in ('XOR', 'OR'):
        errors.add(gate.rightInput.name)

    if len(errors) > 0:
        return False, errors

    left_input_result, left_input_error = check_input_xor(gate.leftInput)
    left_carry_result, left_carry_error = check_carry_or(gate.leftInput)
    if not (left_input_result or left_carry_result):
        errors |= left_input_error | left_carry_error

    right_input_result, right_input_errors = check_input_xor(gate.rightInput)
    right_carry_result, right_carry_errors = check_carry_or(gate.rightInput)
    if not (right_input_result or right_carry_result):
        errors |= right_input_errors | right_carry_errors

    return len(errors) == 0, errors

def check_carry_or(wire: Wire) -> tuple[bool, set[str]]:
    if wire.name == 'mtk': return True, {}
    if wire.source_gate is None: return True, {}
    gate = wire.source_gate
    if gate.type != 'OR': return False, {wire.name}

    errors = set()
    if gate.leftInput.source_gate is not None and gate.leftInput.source_gate.type != 'AND':
        errors.add(gate.leftInput.name)
    
    if gate.rightInput.source_gate is not None and gate.rightInput.source_gate.type != 'AND':
        errors.add(gate.rightInput.name)

    if len(errors) > 0:
        return False, errors

    left_input_result, left_input_error = check_input_and(gate.leftInput)
    left_carry_result, left_carry_error = check_carry_and(gate.leftInput)
    if not (left_input_result or left_carry_result):
        errors |= left_input_error | left_carry_error

    right_input_result, right_input_errors = check_input_and(gate.rightInput)
    right_carry_result, right_carry_errors = check_carry_and(gate.rightInput)
    if not (right_input_result or right_carry_result):
        errors |= right_input_errors | right_carry_errors
    
    return len(errors) == 0, errors

def check_output_xor(wire: Wire) -> tuple[bool, set[str]]:
    if wire.name == 'z00' or wire.name == 'z01': return True, {}
    if wire.source_gate is None: return True, {}
    gate = wire.source_gate
    if gate.type != 'XOR': return False, {wire.name}

    errors = set()
    if gate.leftInput.source_gate is not None and gate.leftInput.source_gate.type not in ('XOR', 'OR'):
        errors.add(gate.leftInput.name)
    
    if gate.rightInput.source_gate is not None and gate.rightInput.source_gate.type not in ('XOR', 'OR'):
        errors.add(gate.rightInput.name)

    if len(errors) > 0:
        return False, errors
    
    left_input_result, left_input_error = check_input_xor(gate.leftInput)
    left_carry_result, left_carry_error = check_carry_or(gate.leftInput)
    if not (left_input_result or left_carry_result):
        errors |= left_input_error | left_carry_error

    right_input_result, right_input_error = check_input_xor(gate.rightInput)
    right_carry_result, right_carry_error = check_carry_or(gate.rightInput)
    if not (right_input_result or right_carry_result):
        errors |= right_input_error | right_carry_error
    
    return len(errors) == 0, errors

class Gate2:
    def __init__(self):
        self.left = None
        self.left_original = None
        self.type = None
        self.right = None
        self.right_original = None
        self.output = None
        self.output_original = None
        self.in_renamed = 0
        self.out_renamed = 0
    
    def __repr__(self):
        return f'{self.left} {self.type} {self.right} -> {self.output}'

def rename_input_gates(gates: list[Gate2]) -> tuple[list[Gate2], list[Gate2]]:
    # Find the input gates
    input_gates = list()
    remaining_gates = list()
    rename_map = dict()
    for gate in gates:
        if gate.left[0] in {'x', 'y'}:
            input_num = gate.left[1:]
            rename_map[gate.output] = gate.type + input_num
            input_gates.append(gate)
        else:
            remaining_gates.append(gate)
    
    do_rename(gates, rename_map)
    return input_gates, remaining_gates

def rename_carry_and_gates(gates: list[Gate2]) -> None:
    rename_map = dict()
    remaining_gates = list()
    for gate in gates:
        if gate.output == 'jjp':
            ...
        if gate.type == 'AND' and gate.in_renamed == 1 and gate.out_renamed == 0:
            if gate.left[:3] == 'XOR':
                num_part = gate.left[3:]
                rename_map[gate.output] = 'CAND' + format(int(num_part), '02')
            elif gate.right[:3] == 'XOR':
                num_part = gate.right[3:]
                rename_map[gate.output] = 'CAND' + format(int(num_part), '02')
            else:
                remaining_gates.append(gate)
        else:
            remaining_gates.append(gate)
    do_rename(gates, rename_map)
    return remaining_gates

def rename_carry_gates(gates: list[Gate2]) -> None:
    rename_map = dict()
    remaining_gates = list()
    for gate in gates:
        if gate.type == 'OR' and gate.in_renamed == 2 and gate.out_renamed == 0:
            if gate.left[:3] == 'AND' and gate.right[:4] == 'CAND':
                num_part = gate.left[3:]
                rename_map[gate.output] = 'CARRY' + format(int(num_part), '02')
            elif gate.right[:3] == 'AND' and gate.left[:4] == 'CAND':
                num_part = gate.right[3:]
                rename_map[gate.output] = 'CARRY' + format(int(num_part), '02')
            else:
                remaining_gates.append(gate)
        else:
            remaining_gates.append(gate)
    
    do_rename(gates, rename_map)
    return remaining_gates

def rename_sum_gates(gates: list[Gate2]) -> list[Gate2]:
    rename_map = dict()
    remaining_gates = list()
    for gate in gates:
        if gate.type == 'XOR' and gate.in_renamed == 2 and gate.out_renamed == 0:
            if gate.left[:3] == 'XOR' and gate.right[:5] == 'CARRY':
                num_part = gate.left[3:]
                rename_map[gate.output] = 'SUM' + num_part
            elif gate.right[:3] == 'XOR' and gate.left[:5] == 'CARRY':
                num_part = gate.right[3:]
                rename_map[gate.output] = 'SUM' + num_part
            else:
                remaining_gates.append(gate)
        else:
            remaining_gates.append(gate)
    
    do_rename(gates, rename_map)
    return remaining_gates

def do_rename(gates: list[Gate2], rename_map: dict[str, str], count: bool = True) -> None:
    for gate in gates:
        for gate in gates:
            if gate.left in rename_map:
                gate.left = rename_map[gate.left]
                if count: gate.in_renamed += 1
            if gate.right in rename_map:
                gate.right = rename_map[gate.right]
                if count: gate.in_renamed += 1
            if gate.output in rename_map:
                gate.output = rename_map[gate.output]
                if count: gate.out_renamed += 1

def check_carry_and_gates(gates: list[Gate2]) -> list[str]:
    and_gates = [gate for gate in gates if gate.type == 'AND']

    problem_wires = list()
    for gate in and_gates:
        if gate.left[:3] != 'XOR' and gate.left[:5] != 'CARRY' and gate.left[0] not in {'x', 'y'}:
            problem_wires.append(gate.left_original)
        
        if gate.right[:3] != 'XOR' and gate.right[:5] != 'CARRY' and gate.right[0] not in {'x', 'y'}:
            problem_wires.append(gate.right_original)
    
    return problem_wires

def check_carry_or_gates(gates: list[Gate2]) -> list[str]:
    or_gates = [gate for gate in gates if gate.type == 'OR']

    problem_wires = list()
    for gate in or_gates:
        if gate.left[:3] != 'AND' and gate.left[:4] != 'CAND':
            problem_wires.append(gate.left_original)
        
        if gate.right[:3] != 'AND' and gate.right[:4] != 'CAND':
            problem_wires.append(gate.right_original)

    return problem_wires

def check_AND_gates(gates: list[Gate2]) -> list[Gate2]:
    process_gates: list[Gate2] = [gate for gate in gates if gate.output[:3] == 'AND']
    missing_gates = list()

    for n in range(45):
        expected_name = 'AND' + format(n, '02')
        expected_gate = [gate for gate in process_gates if gate.output == expected_name]
        if len(expected_gate) != 1:
            missing_gates.append(expected_name)
    
    return missing_gates

def check_XOR_gates(gates: list[Gate2]) -> list[Gate2]:
    process_gates: list[Gate2] = [gate for gate in gates if gate.output[:3] == 'XOR']
    missing_gates = list()

    for n in range(45):
        expected_name = 'XOR' + format(n, '02')
        expected_gate = [gate for gate in process_gates if gate.output == expected_name]
        if len(expected_gate) != 1:
            missing_gates.append(expected_name)
    
    return missing_gates

def check_CAND_gates(gates: list[Gate2]) -> list[Gate2]:
    process_gates: list[Gate2] = [gate for gate in gates if gate.type == 'AND' and gate.output[:3] != 'AND']
    missing_gates = list()
    problem_wires = list()

    for n in range(45):
        expected_name = 'CAND' + format(n, '02')
        expected_gate = [gate for gate in process_gates if gate.output == expected_name]
        if len(expected_gate) == 1:
            gate = expected_gate[0]
            expected_xor = 'XOR' + format(n, '02')
            expected_carry = 'CARRY' + format(n-1, '02')
            if gate.left[:3] != expected_xor and gate.left[:5] != expected_carry:
                problem_wires.append(gate.left_original)
        
            if gate.right[:3] != expected_xor and gate.right[:5] != expected_carry:
                problem_wires.append(gate.right_original)
        else:
            missing_gates.append(expected_name)
    
    return missing_gates

def find_gates_with_input(gates: list[Gate2], input_name: str) -> list[Gate2]:
    ret = [gate for gate in gates if input_name in {gate.left, gate.right, gate.left_original, gate.right_original}]
    return ret


def find_gates_with_name(gates: list[Gate2], input_name: str) -> list[Gate2]:
    ret = [gate for gate in gates if input_name in {gate.left, gate.right, gate.left_original, gate.right_original, gate.output, gate.output_original}]
    return ret

def process_data(data: str) -> list[str]:
    gate_strs = data.split('\n\n')[1]

    gates: list[Gate2] = list()
    for line in gate_strs.splitlines():
        parts = re.match(r'(...) (AND|OR|XOR) (...) -> (...)', line)
        gate = Gate2()
        gate.left = parts[1]
        gate.left_original = parts[1]
        gate.type = parts[2]
        gate.right = parts[3]
        gate.right_original = parts[3]
        gate.output = parts[4]
        gate.output_original = parts[4]
        gates.append(gate)

    
    input_gates, remaining_gates = rename_input_gates(gates)
    do_rename(gates, {'AND00': 'CARRY00'}, False)
    remaining_gates = rename_carry_and_gates(gates)
    do_rename(gates, {'jjp': 'CAND01'}, True)
    remaining_gates = rename_carry_gates(gates)
    remaining_gates = rename_sum_gates(gates)
    # known_good_renames = {
    #     'AND00': 'CARRY00',
    #     'jjp': 'CAND01',
    #     # 'cqp': 'CARRY01',
    #     # 'trv': 'CAND02',
    # }
    # do_rename(gates, known_good_renames, False)

    problems: set[str] = set()
    #ret = check_half_adder(gates, 0)
    #problems.update(ret)

    for n in range(45):
        name = f'z{format(n, '02')}'
        print(find_gates_with_name(gates, name))

    for n in range(1,45):
        original_name = f'z{format(n, '02')}'
        output_name = f'SUM{format(n, '02')}'
        gate = [gate for gate in gates if gate.output_original == original_name][0]
        if gate.output != output_name:
            print(f'error: {gate}')
    # STOP HERE - The print statement above gives enough information to solve by hand.
    # The answer is: frn,gmq,vtj,wnf,wtt,z05,z21,z39

    # gates with 3 renames should be OK
    remaining_gates = [gate for gate in gates if (gate.in_renamed != 2 or gate.out_renamed != 1) and gate.left[0] not in {'x', 'y'} and gate.output != 'z01']

    # ret = check_AND_gates(gates)
    # problems.update(ret)
    # ret = check_XOR_gates(gates)
    # problems.update(ret)
    # ret = check_CAND_gates(gates)
    # problems.update(ret)
    # print(','.join(sorted(problems)))

    # problem_wires = set()
    # ret = check_carry_and_gates(gates)
    # problem_wires |= set(ret)
    # ret = check_carry_or_gates(gates)
    # problem_wires |= set(ret)

    # print(','.join(sorted(problem_wires)))


    ...

def d24p2(data: str) -> int:

    wrong_wires = process_data(data)
    
    wires = parseData(data)

    x_names = get_names(wires, 'x')
    y_names = get_names(wires, 'y')
    z_names = get_names(wires, 'z')
    names_list = [x_names, y_names, z_names]

    # inputs = get_inputs(wires['z07'])
    # for input in sorted(map(lambda x: x.name, inputs)):
    #     print(input)

    for name in z_names:
        check_output_xor(wires[name])

    wires['z03'].get_value()
    # find_structure_errors(wires, 2)

    pairs = set()
    bad_set = set()

    for power in range(45):
        bad_wires = test_value(wires, power, names_list)
        if len(bad_wires) > 0:
            # find the swap that fixes things
            bad_wires -= set(x_names)
            bad_wires -= set(y_names)
            bad_wires -= set(z_names)
            for w1, w2 in combinations(bad_wires, 2):
                # swap two wires
                swap_wires(wires, w1, w2)
                
                # test if the result is good. If it is, break, otherwise undo the swap and continue
                test_bad_wires = set()
                for p in range(power+1):
                    try:
                        test_bad_wires |= test_value(wires, p, names_list)
                    except RecursionError:
                        test_bad_wires.add('RecursionFault')
                        break
                if len(test_bad_wires) > 0:
                    # no good
                    swap_wires(wires, w1, w2)
                else:
                    pairs.add((w1, w2))
                    bad_set.add(w1)
                    bad_set.add(w2)
                    swap_wires(wires, w1, w2)
        ...

    bad_wires -= set(x_names)
    bad_wires -= set(y_names)
    bad_wires -= set(z_names)



    return ','.join(list(sorted(bad_wires)))

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
    result = d24p2(data)
    print(result)