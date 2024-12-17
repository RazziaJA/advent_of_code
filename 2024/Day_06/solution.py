import copy

#filename = "sample.txt" # expected: 41 and 6
filename = "input.txt"

grid = []
with open(filename) as f:
    grid = [list(line.rstrip()) for line in f]

W = len(grid[0])
H = len(grid)

curx,cury = -1,-1
for yidx, line in enumerate(grid):
    for xidx, c in enumerate(line):
        if c == '^':
            curx = xidx
            cury = yidx
            break

# Returns bool,int representing loop?, visited_tiles_count
def traverse(curx, cury, grid):
    visited = copy.deepcopy(grid)
    turns = {'^': [], '>': [], 'v':[], '<':[]}
    visited[cury][curx] = 'X'
    visit_count = 1
    dir = '^'
    nextx,nexty = curx,cury-1
    while (0 <= nextx < W and 0 <= nexty < H):
        if grid[nexty][nextx] != '#':
            curx,cury = nextx,nexty
            if visited[cury][curx] != 'X':
                visited[cury][curx] = 'X'
                visit_count += 1
        else:
            # Have we hit this obstruction facing this direction before?
            if (curx, cury) in turns[dir]:
                return True, visit_count
            else:
                turns[dir].append((curx, cury))

            match dir:
                case '^':
                    dir = '>'
                case '>':
                    dir = 'v'
                case 'v':
                    dir = '<'
                case '<':
                    dir = '^'
        match dir:
                case '^':
                    nextx,nexty = curx,cury-1
                case '>':
                    nextx,nexty = curx+1,cury
                case 'v':
                    nextx,nexty = curx,cury+1
                case '<':
                    nextx,nexty = curx-1,cury
    return False, visit_count

looped, visit_count = traverse(curx, cury, grid)
print(f"Part 1: {visit_count}")

loop_count = 0
obstructed = copy.deepcopy(grid)
for obsy in range(H):
    print(f"Checking row: {obsy}")
    for obsx in range(W):
        if grid[obsy][obsx] == '#' or grid[obsy][obsx] == '^':
            continue
        obstructed[obsy][obsx] = '#'
        looped, visit_count = traverse(curx, cury, obstructed)
        obstructed[obsy][obsx] = grid[obsy][obsx]
        if looped:
            loop_count += 1

print(f"Part 2: {loop_count}")