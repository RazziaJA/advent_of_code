#filename = "sample.txt" # expected: 14, 34
filename = "input.txt"

lines = None
with open(filename) as f:
    lines = [line.rstrip() for line in f]

H = len(lines)
W = len(lines[0])

freq_map = {}
for y in range(H):
    for x in range(W):
        if lines[y][x] != '.':
            c = lines[y][x]
            if c not in freq_map:
                freq_map[c] = []
            freq_map[c].append((x,y))

def find_antinodes(p1, p2):
    ret = []
    x1,y1 = p1
    x2,y2 = p2
    adx = abs(x2-x1)
    ady = abs(y2-y1)
    #vertical
    if min(x1,x2) == max(x1,x2):
        y3 = min(y1,y2) - ady
        y4 = max(y1,y2) + ady
        if 0 <= y3 < H:
            ret.append((x1,y3))
        if 0 <= y4 < H:
            ret.append((x1,y4))
    else:
        m = (y2-y1)/(x2-x1)
        x3 = min(x1,x2) - adx
        y3 = min(y1,y2) - ady if m >= 0 else max(y1,y2) + ady
        x4 = max(x1,x2) + adx
        y4 = max(y1,y2) + ady if m >= 0 else min(y1,y2) - ady
        if 0 <= x3 < W and 0 <= y3 < H:
            ret.append((x3,y3))
        if 0 <= x4 < W and 0 <= y4 < H:
            ret.append((x4,y4))
    return ret

def find_antinodes_part2(p1, p2):
    ret = []
    x1,y1 = p1
    x2,y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    #vertical
    if dx == 0:
        for y in range(H):
            ret.append((x1,y))
    else:
        x,y = x1,y1
        #backwards
        while (0 <= x < W and 0 <= y < H):
            ret.append((x,y))
            x -= dx
            y -= dy
        x,y = x1,y1
        #forwards
        while (0 <= x < W and 0 <= y < H):
            ret.append((x,y))
            x += dx
            y += dy
    return ret

antinodes = set()
antinodes2 = set()
for nodes in freq_map.values():
    for l in range(len(nodes)):
        for r in range(l+1, len(nodes)):
            ans = find_antinodes(nodes[l], nodes[r])
            for an in ans:
                antinodes.add(an)
            ans2 = find_antinodes_part2(nodes[l], nodes[r])
            for an in ans2:
                antinodes2.add(an)

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes2)}")