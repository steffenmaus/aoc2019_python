class IntCodeComputer:
    def __init__(self, intcode):
        self.inputs = []
        self.input_pointer = 0
        self.outputs = []
        self.pointer = 0
        self.successor = None
        self.memory = {}
        self.relative_base = 0
        for k, v in enumerate(intcode.split(',')):
            self.memory[k] = int(v)

    def add(self, e):
        self.inputs.append(e)

    def add_ascii_line(self, line):
        for c in line:
            self.inputs.append(ord(c))
        self.inputs.append(10)

    def set_successor(self, icc):
        self.successor = icc

    def get_next_input(self):
        if self.input_pointer >= len(self.inputs):
            return None
        res = self.inputs[self.input_pointer]
        self.input_pointer += 1
        return res

    def get_from_mem(self, pos):
        if not self.memory.get(pos):
            return 0
        else:
            return self.memory.get(pos)

    def set_mem(self, pos, val):
        self.memory[pos] = val

    def get_next_block(self):
        pre = self.memory.get(self.pointer)
        opcode = pre % 100
        params = []
        for i in range(1, 4):
            mode = (pre // 10 ** (i + 1)) % 10
            match mode:
                case 0:
                    params.append(self.get_from_mem(self.pointer + i))
                case 1:
                    params.append(self.pointer + i)
                case 2:
                    params.append(self.get_from_mem(self.pointer + i) + self.relative_base)

        return opcode, params

    def run(self):
        while True:
            opcode, params = self.get_next_block()
            match opcode:
                case 1:
                    self.memory[params[2]] = self.get_from_mem(params[0]) + self.get_from_mem(params[1])
                    self.pointer += 4
                case 2:
                    self.memory[params[2]] = self.get_from_mem(params[0]) * self.get_from_mem(params[1])
                    self.pointer += 4
                case 3:
                    next_input = self.get_next_input()
                    if next_input is None:
                        return -1
                    else:
                        self.memory[params[0]] = next_input
                        self.pointer += 2
                case 4:
                    self.outputs.append(self.get_from_mem(params[0]))
                    if self.successor is not None:
                        self.successor.add(self.outputs[-1])
                    self.pointer += 2
                case 5:
                    if self.get_from_mem(params[0]) != 0:
                        self.pointer = self.get_from_mem(params[1])
                    else:
                        self.pointer += 3
                case 6:
                    if self.get_from_mem(params[0]) == 0:
                        self.pointer = self.get_from_mem(params[1])
                    else:
                        self.pointer += 3
                case 7:
                    if self.get_from_mem(params[0]) < self.get_from_mem(params[1]):
                        self.memory[params[2]] = 1
                    else:
                        self.memory[params[2]] = 0
                    self.pointer += 4
                case 8:
                    if self.get_from_mem(params[0]) == self.get_from_mem(params[1]):
                        self.memory[params[2]] = 1
                    else:
                        self.memory[params[2]] = 0
                    self.pointer += 4
                case 9:
                    self.relative_base += self.get_from_mem(params[0])
                    self.pointer += 2
                case 99:
                    break
                case _:
                    print("Unknown opcode: " + str(opcode))
                    exit(1)
