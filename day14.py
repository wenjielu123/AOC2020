import re
from utils.io_util import read_file

# input_path = 'inputs/day14_test.txt'
input_path = 'inputs/day14.txt'

instructions = read_file(input_path)

def apply_bitmask(addr_in, bitmask):
    """Both value and bitmask are 36-bit string"""
    addrs_out = ['']
    for x, m in zip(addr_in, bitmask):
        addrs_out_new = []
        if m == '0':
            for i in range(len(addrs_out)):
                addrs_out_new.append(addrs_out[i] + x)
        elif m == '1':
            for i in range(len(addrs_out)):
                addrs_out_new.append(addrs_out[i] + '1')
        elif m == 'X':
            for i in range(len(addrs_out)):
                addrs_out_new.append(addrs_out[i] + '0')
                addrs_out_new.append(addrs_out[i] + '1')
        addrs_out = addrs_out_new

    return addrs_out

def apply_instrs(instructions):
    bitmask = ''
    memory = {}
    for instr in instructions:
        if 'mask' in instr:
            bitmask = re.findall(r'mask = ([\dX]+)', instr)[0]
        else:
            addr, value = re.findall(r'mem\[([\d]+)\] = ([\d]+)', instr)[0]
            addr = '{:036b}'.format(int(addr))
            addrs = apply_bitmask(addr, bitmask)
            
            for addr in addrs:
                memory[int(addr, 2)] = int(value)

    return memory

memory = apply_instrs(instructions)

res = sum([memory[k] for k in memory])
print(res)