import re
from pathlib import Path


def read_file(input_path):
    with open(input_path, 'r') as f:
        string = f.read().splitlines()
    
    return string

def process_passports(inputs):
    passports = []
    passport = {}
    for input in inputs:
        if input:
            fields = input.split(' ')
            for field in fields:
                k, v = field.split(':')
                passport[k] = v
        else: # meet an empty line
            passports.append(passport)
            passport = {}

    passports.append(passport)
    return passports

def val_byr(byr):
    return 1920 <= int(byr) <= 2002

def val_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def val_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def val_hgt(hgt):
    if 'cm' in hgt:
        return 150 <= int(hgt[:-2]) <= 193
    elif 'in' in hgt:
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False

def val_hcl(hcl):
    return re.fullmatch(r'#[0-9a-f]{6}', hcl) is not None

def val_ecl(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def val_pid(pid):
    return re.fullmatch(r'\d{9}', pid) is not None

def count_valid(passports):
    nvalid = 0
    for passport in passports:
        valid = True
        valid *= all([k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')])

        if valid: 
            valid = (val_byr(passport['byr']) *
                     val_iyr(passport['iyr']) *
                     val_eyr(passport['eyr']) *
                     val_hgt(passport['hgt']) *
                     val_hcl(passport['hcl']) *
                     val_ecl(passport['ecl']) *
                     val_pid(passport['pid'])
                    )
        if valid:
            nvalid += 1
    return nvalid

input_path = Path('inputs/day4_test.txt')
input_path = Path('inputs/day4.txt')
inputs = read_file(input_path)

passports = process_passports(inputs)
nvalid = count_valid(passports)
print(nvalid)
