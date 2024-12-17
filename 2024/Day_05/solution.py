#filename = "sample.txt"
filename = "input.txt"

# key must precede all entries in val_list
rules = {}
updates = []
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            continue
        if '|' in line:
            k,v = line.split('|')
            if k not in rules:
                rules[k] = []
            rules[k].append(v)
        else:
            updates.append(line.split(','))

def is_good(update):
    seen = []
    for page in update:
        if page in rules and any(v in seen for v in rules[page]):
            return False
        seen.append(page)
    return True

def fix(update):
    fixed = update.copy()
    while (not is_good(fixed)):
        seen = []
        for page in fixed:
            if page in rules and any(v in seen for v in rules[page]):
                prob = next(s for s in seen if s in rules[page])
                fixed.remove(page)
                fixed.insert(fixed.index(prob), page)
                break
            seen.append(page)
    return fixed

total = 0
bad_updates = []
for update in updates:
    if is_good(update):
        total += int(update[len(update)//2])
    else:
        bad_updates.append(update)

print (f"Part 1: {total}")

total = 0
for update in bad_updates:
    fixed = fix(update)
    total += int(fixed[len(fixed)//2])

print (f"Part 2: {total}")
