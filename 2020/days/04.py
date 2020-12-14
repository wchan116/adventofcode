from utils import get_input

import re


def check_fields_present(passport):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    return len(passport.keys()) == len(fields) or (
        len(passport.keys()) == len(fields) - 1 and "cid" not in passport.keys()
    )


def check_valid_birth(passport):
    return 1920 <= int(passport["byr"]) <= 2002


def check_valid_issue(passport):
    return 2010 <= int(passport["iyr"]) <= 2020


def check_valid_expiry(passport):
    return 2020 <= int(passport["eyr"]) <= 2030


def check_valid_height(passport):
    hm = re.match(r"^(\d+)(cm|in)$", passport["hgt"])
    if not hm:
        return False
    cm_pred = hm.group(2) == "cm" and 150 <= int(hm.group(1)) <= 193
    in_pred = hm.group(2) == "in" and 59 <= int(hm.group(1)) <= 76
    if not (cm_pred or in_pred):
        return False
    return True


def check_valid_hair(passport):
    return re.match(r"^#[0-9a-f]{6}$", passport["hcl"])


def check_valid_eye(passport):
    return passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def check_valid_passport(passport):
    return re.match(r"^\d{9}$", passport["pid"])


def check_valid_fields(passport):
    return (
        check_fields_present(passport)
        and check_valid_birth(passport)
        and check_valid_issue(passport)
        and check_valid_expiry(passport)
        and check_valid_height(passport)
        and check_valid_hair(passport)
        and check_valid_eye(passport)
        and check_valid_passport(passport)
    )


def count_valid_passports(passports, pred):
    return sum(1 for passport in passports if pred(passport))


def p1(inp):
    return count_valid_passports(get_passports(inp), check_fields_present)


def p2(inp):
    return count_valid_passports(get_passports(inp), check_valid_fields)


def get_passports(inp):
    passports = []
    passport = {}
    for line in inp:
        if line == "":
            passports.append(passport)
            passport = {}
            continue

        entries = line.split()
        for entry in entries:
            key, value = entry.split(":")
            passport[key] = value
    passports.append(passport)
    return passports


inp = get_input()
print(p1(inp))
print(p2(inp))
