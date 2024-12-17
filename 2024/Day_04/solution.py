grid = []
filename = "input.txt"
#filename = "sample.txt"
with open(filename) as f:
    grid = [line.rstrip() for line in f]

H = len(grid)
W = len(grid[0])
TARGET = "XMAS"

def matches_from_cell(grid, x, y, target = TARGET):
    if (x < 0 or x >= W or y < 0 or y >= H):
        return False
    if (grid[y][x] != target[0]):
        return 0
    found = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 and dy == 0):
                continue
            found += 1 if check_dir(grid, x+dx, y+dy, dx, dy, target[0], target) else 0
    return found

def check_dir(grid, x, y, dx, dy, cur = '', target = TARGET):
    if (x < 0 or x >= W or y < 0 or y >= H):
        return False
    if (grid[y][x] != target[len(cur)]):
        return False
    cur = cur + target[len(cur)]
    if (cur == target):
        return True
    return check_dir(grid, x+dx, y+dy, dx, dy, cur, target)

total = 0
for x in range(W):
    for y in range(H):
        matches = matches_from_cell(grid, x, y, TARGET)
        total += matches

print (f"Part 1: {total}")

def check_cell_2(grid, x, y):
    C = grid[y+1][x+1]
    if (C != 'A'):
        return 0
    TL = grid[y][x]
    TR = grid[y][x+2]
    BL = grid[y+2][x]
    BR = grid[y+2][x+2]
    count = 1 if ((TL == 'M' or TL == 'S') and (BR == 'M' or BR == 'S') and (TL != BR)) else 0
    count += 1 if ((TR == 'M' or TR == 'S') and (BL == 'M' or BL == 'S') and (TR != BL)) else 0
    # if (count > 0):
    #     print (f"{count} at ({x},{y})")
    #     print (f"\t{TL}_{TR}")
    #     print (f"\t_{C}_")
    #     print (f"\t{BL}_{BR}")
    return 1 if count == 2 else 0

total = 0
for x in range(W-2):
    for y in range(H-2):
        total += check_cell_2(grid, x, y)

print(f"Part 2: {total}")
    