import math
from utils.io_util import read_file
from functools import reduce

# input_path = 'inputs/day13_test.txt'
input_path = 'inputs/day13.txt'

inputs = read_file(input_path)
time0 = int(inputs[0])
buses = inputs[1]

def find_wait_times(time0, buses):
    wait_times = {}
    min_wait_times = math.inf
    ans = 0

    for bus in buses:
        if bus == 'x':
            continue
        else:
            bus = int(bus)
            k = math.ceil(time0 / bus)
            wait_time = bus * k - time0
            wait_times[bus] = wait_time
            
            if wait_time < min_wait_times:
                min_wait_times = wait_time
                ans = bus * min_wait_times

    return wait_times, ans

def exgcd(a, b):
    """Extended Euclidean Algorithm, return the solution of:
    gcd(a, b) = s*a + t*b

    Return: gcd(a,b), s, t
    """
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while (r1 % r2 != 0):
        q = r1 // r2
        r = r1 % r2
        r1, r2 = r2, r
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    
    return r2, s2, t2

def modInverse(a, m):
    """Find the modulo inverse x of a mod m, such that
    a*x == 1 (mod m)
    """
    gcd, s, _ = exgcd(a, m)
    assert gcd == 1, "modInverse must be coprime"
    return s

def chinese_remainder_algo(modulos, remainders):
    """Solve the Chinese Remainder Algorithm"""
    N = 1
    for n in modulos:
        N *= n

    x = 0
    for mi, ai in zip(modulos, remainders):
        yi = N // mi  # critical to take integer division!!!
        zi = modInverse(yi, mi)
        x += ai * yi * zi 

    return int(x) % N

def find_timestamp(buses):
    remainders = []
    modulos = []
    buses = buses.split(',')
    for i, bus in enumerate(buses):
        if bus != 'x':
            m = int(bus)
            k = math.ceil(i / m)
            r = k * m - i
            remainders.append(r)
            modulos.append(m)

    return chinese_remainder_algo(modulos, remainders)

buses_list = ['17,x,13,19', '67,7,59,61', '67,x,7,59,61', '67,7,x,59,61', '1789,37,47,1889']
assert find_timestamp(buses_list[0]) == 3417
assert find_timestamp(buses_list[1]) == 754018
assert find_timestamp(buses_list[2]) == 779210
assert find_timestamp(buses_list[3]) == 1261476
assert find_timestamp(buses_list[4]) == 1202161486

ans = find_timestamp(buses)
print(ans)
assert ans % 23 == 0
assert ans % 41 == 28