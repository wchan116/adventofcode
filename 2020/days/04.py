import re

passports = []
fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid'
        }

with open('input/04.in') as f:
    passport = {}
    for line in f.readlines():
        if line == '\n':
            passports.append(passport)
            passport = {}
            continue

        entries = line.split()
        for entry in entries:
            #print(line)
            key, value = entry.split(':')
            passport[key] = value
    passports.append(passport)
 
def p1(p):
    valid = 0
    for passport in p:
        if len(passport.keys()) == len(fields) or (len(passport.keys()) == len(fields) - 1 and 'cid' not in passport.keys()):
            valid += 1
    return valid

def p2(p):
    valid = 0
    for passport in p:
        if not (len(passport.keys()) == len(fields) or (len(passport.keys()) == len(fields) - 1 and 'cid' not in passport.keys())):
            continue
        if not (1920 <= int(passport['byr']) <= 2002):
            continue
        if not (2010 <= int(passport['iyr']) <= 2020):
            continue
        if not (2020 <= int(passport['eyr']) <= 2030):
            continue
        hm = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
        if not hm:
            continue
        else:
            cm_pred = hm.group(2) == 'cm' and 150 <= int(hm.group(1)) <= 193
            in_pred = hm.group(2) == 'in' and 59 <= int(hm.group(1)) <= 76
            if not (cm_pred or in_pred):
                continue
        hclm = re.match(r'^#[0-9a-f]{6}$', passport['hcl'])
        if not hclm:
            continue
        if not (passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
            continue
        pidm = re.match(r'^\d{9}$', passport['pid'])
        if not pidm:
            continue
        valid += 1
    return valid

print(p1(passports))
print(p2(passports))
