def is_safe(levels):
    if len(levels) < 2:
        return True
    if (levels[0] == levels[1]):
        return False
    
    prev = levels[0]
    asc = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        dif = levels[i] - levels[i-1]
        if (dif == 0):
            return False
        if (asc != (dif > 0)):
            return False
        if (abs(dif) < 1 or abs(dif) > 3):
            return False
    return True

safe_count = 0
with open("input.txt") as f:
    for report in f:
        levels = [int(x) for x in report.split(' ')]
        safe_count += 1 if is_safe(levels) else 0

print(f"Part 1: {safe_count}")

def is_safe_2(levels, dampen_idx=None):
    if (dampen_idx != None):
        dampened = levels.copy()
        del dampened[dampen_idx]
        return is_safe_2(dampened)
    if len(levels) < 2:
        return True
    if (levels[0] == levels[1]):
        return False
    
    prev = levels[0]
    asc = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        dif = levels[i] - levels[i-1]
        if (dif == 0):
            return False
        if (asc != (dif > 0)):
            return False
        if (abs(dif) < 1 or abs(dif) > 3):
            return False
    return True

safe_count_2 = 0
with open("input.txt") as f:
    for report in f:
        levels = [int(x) for x in report.split(' ')]
        safe = is_safe_2(levels)
        if (safe == False):
            for i in range(len(levels)):
                safe = is_safe_2(levels, i)
                if safe:
                    break
        safe_count_2 += 1 if safe else 0

print(f"Part 2: {safe_count_2}")