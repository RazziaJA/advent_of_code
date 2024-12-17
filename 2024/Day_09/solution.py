filename = "sample.txt" # expected: 1928, 2858
#filename = "input.txt"


def diskmap():
    with open(filename) as f:
        diskmap = [int(c) for c in f.readline().rstrip()]
    return diskmap

def map_to_mem(diskmap, ids=None):
    mem = []
    for idx,n in enumerate(diskmap):
        val = None if idx%2 == 1 else idx//2 if ids == None else ids[idx//2]
        for i in range(n):
            mem.append(val)
    return mem
        
def compact(mem_in):
    mem = mem_in.copy()
    l,r = 0,len(mem)-1
    while mem[r] == None:
        r -= 1
    while mem[l] != None:
        l += 1
    
    while (l < r):
        mem[l] = mem[r]
        mem[r] = None
        while mem[r] == None:
            r -= 1
        while mem[l] != None:
            l += 1
    return mem, r+1

def checksum(mem, end):
    checksum = 0
    for i in range(end):
        checksum += i*mem[i] if mem[i] != None else 0
    return checksum


print(f"Part 1: {checksum(*compact(map_to_mem(diskmap())))}")

# returns newdiskmap,idslist
def compact2(diskmap):
    ids = [i//2 for i in range(0,len(diskmap),2)]
    idx = len(diskmap)-1
    for fileid in range(idx//2, -1, -1):
        size = diskmap[idx]
        #print(f"Checking to move file ID={fileid} of size {size} from index {idx}")
        for i in range(1, idx, 2):
            if diskmap[i] >= size:
                if idx+1 < len(diskmap):
                    diskmap[idx-1] += diskmap[idx+1]
                    del diskmap[idx+1]
                diskmap[idx-1] += diskmap[idx]
                del diskmap[idx]

                space = diskmap[i]
                print(f"Should fit in the space at index {i} of size {space}")
                diskmap[i] = 0
                diskmap.insert(i+1, size)
                diskmap.insert(i+2, space-size)

                print(f"Changing file order\n\tmoving file {fileid} from index {ids.index(fileid)} to index {(i+1)//2}")
                ids.remove(fileid)
                ids.insert((i+1)//2, fileid)

                print("".join(map(str,diskmap)))
                #print("".join(map(str, map_to_mem(diskmap, ids))).replace("None", '.') + " |\t" + "".join(map(str, ids)))
                idx += 2
                break
        idx -= 2

# 23  33133121414131402
# 20213313312141413142
goal_for_sample= "20201030312134414542"

# 00992111777.44.333....5555.6666.....8888..
compact2(diskmap())
print(str(goal_for_sample))