import re
from pathlib import Path

# -------------------------
# byr(Birth Year)
# iyr(Issue Year)
# eyr(Expiration Year)
# hgt(Height)
# hcl(Hair Color)
# ecl(Eye Color)
# pid(Passport ID)
# cid(Country ID)
# -------------------------
# byr(BirthYear) - four digits; at least 1920 and at most 2002.
# iyr(IssueYear) - four digits; at least 2010 and at most 2020.
# eyr(ExpirationYear) - four digits; at least 2020 and at most 2030.
# hgt(Height) - a number followed by either cm or in:
#                 - If cm, the number must be at least 150 and at most 193.
#                 - If in, the number must be at least 59 and at most 76.
# hcl(HairColor) - a  # followed by exactly six characters 0-9 or a-f.
# ecl(EyeColor) - exactly oneo f: amb blu brn gry grn hzl oth.
# pid(PassportID) - a nine - digitnumber, including leading zeroes.
# cid(CountryID) - ignored, missing or not.
# -------------------------


keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
emptyLine_pattern = r"\n\s*\n"
passports = [p for p in re.split(emptyLine_pattern, Path("input.txt").read_text().strip()) if len(p) > 1]


def checkValidExtended(passport: str) -> bool:
    valid = True
    digits = ["byr", "iyr", "eyr", "pid"]
    pattern = r"[\s\n]+"
    keys_and_values = re.split(pattern, passport)
    dict_keys_values = {}
    ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for kv in keys_and_values:
        (key, value) = kv.split(":")
        dict_keys_values[key] = value
    for d in digits:
        if not dict_keys_values[d].isdigit():
            return False
    for k in keys:
        if k == "byr":
            if int(dict_keys_values[k]) < 1920 or int(dict_keys_values[k]) > 2002:
                return False
        if k == "iyr":
            if int(dict_keys_values[k]) < 2010 or int(dict_keys_values[k]) > 2020:
                return False
        if k == "eyr":
            if int(dict_keys_values[k]) < 2020 or int(dict_keys_values[k]) > 2030:
                return False
        if k == "hgt":
            if bool(re.match(r"[0-9]{2}in", dict_keys_values[k])):
                if int(dict_keys_values[k][:2]) < 59 or int(dict_keys_values[k][:2]) >76:
                    return False
            elif bool(re.match(r"[0-9]{3}cm", dict_keys_values[k])):
                if int(dict_keys_values[k][:3]) < 150 or int(dict_keys_values[k][:3]) > 193:
                    return False
            else:
                return False
        if k == "hcl":
            if not bool(re.match(r"^#[0-9a-z]{6}$", dict_keys_values[k])):
                return False
        if k == "ecl":
            if not bool(re.match(r"^[a-z]{3}$", dict_keys_values[k])) or dict_keys_values[k] not in ecl_values:
                return False
        if k == "pid":
            if not bool(re.match(r"^[0-9]{9}$", dict_keys_values[k])):
                return False
    return True


def checkValidPassports() -> (int, int):
    """
    :return: (Number of valid passports, Number of valid passports with extended security)
    """
    counter = 0
    counter_extended = 0
    for passport in passports:
        valid = True
        for key in keys:
            if key + ":" != "cid:":
                if key + ":" not in passport:
                    valid = False
                    break
        if valid:
            counter += 1
            if checkValidExtended(passport):
                counter_extended += 1
    return (counter, counter_extended)


validCount, validCount_extended = checkValidPassports()
print("first task: ", validCount, "\nsecond task: ", validCount_extended)

