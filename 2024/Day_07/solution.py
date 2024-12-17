#filename = "sample.txt" # expected: 3749, 11387
filename = "input.txt"


def add(l,r):
    return l+r
def mult(l,r):
    return l*r
def concat(l,r):
    return int(str(l) + str(r))

def check(target, args, ops, idx=None, val=None):
    if idx == None and val == None:
        val = args[0]
        idx = 1
    if idx >= len(args):
        return val == target
    
    for op in ops:
        if check(target, args, ops, idx+1, op(val, args[idx])):
            return True
    return False
    

p1_total = 0
p2_total = 0
with open(filename) as f:
    for line in f:
        target, args = line.rstrip().split(': ')
        target = int(target)
        args = [int(n) for n in args.split(' ')]
        if check(target, args, [add, mult]):
            p1_total += target
        if check(target, args, [add, mult, concat]):
            p2_total += target

print(f"Part 1: {p1_total}")
print(f"Part 2: {p2_total}")