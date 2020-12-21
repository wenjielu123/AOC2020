import time
from pathlib import Path

def read_file_raw(input_path):
    with open(Path(input_path), 'r') as f:
        string = f.read()
    
    return string
    
def read_file(input_path):
    with open(Path(input_path), 'r') as f:
        string = f.read().splitlines()
    
    return string

def read_file_with_emptyline(input_path):
    with open(Path(input_path), 'r') as f:
        string = f.read().split('\n\n')
    
    output = []
    for line in string:
        output.append(line.split('\n'))
    return output

def console_decode_line(line):
    """Read a line of the program, and return the line_increment, and accumulator_increment"""
    op, num = line.split(' ')
    if op == 'nop':
        return 1, 0
    elif op == 'acc':
        return 1, int(num)
    elif op == 'jmp':
        return int(num), 0
    else:
        raise ValueError(f'op {op} is invalid.')



class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")