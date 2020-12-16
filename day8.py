from utils.io_util import read_file, console_decode_line


input_file = 'inputs/day8_test.txt'
input_file = 'inputs/day8.txt'
inputs = read_file(input_file)

def console_run(lines):
    line_curr_idx = 0
    line_indices = []
    accumulator = 0

    while line_curr_idx not in line_indices and line_curr_idx < len(lines):
        line_indices.append(line_curr_idx)
        line_inc, acc_inc = console_decode_line(lines[line_curr_idx])

        line_curr_idx += line_inc
        accumulator += acc_inc

    return line_curr_idx, accumulator

def fix_console(lines):
    for i, line in enumerate(lines):
        if 'nop' in line or 'jmp' in line:
            if 'nop' in line:
                line_new = line.replace('nop', 'jmp')
            elif 'jmp' in line: 
                line_new = line.replace('jmp', 'nop')
            
            lines_new = lines[:i] + [line_new] + lines[i+1:]
            line_curr_idx, accumulator = console_run(lines_new)
            if line_curr_idx == len(lines):
                print(f'Success! Acc = {accumulator}')

fix_console(inputs)
        