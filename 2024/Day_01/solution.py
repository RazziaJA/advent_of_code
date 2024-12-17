l1 = []
l2 = []

with open("input.txt") as f:
    for line in f:
        l, r = line.split("   ")
        l1.append(int(l))
        l2.append(int(r))

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])

print(f"Part 1: {sum}")

sim_score = 0
for n in l1:
    sim_score += n * l2.count(n)

print(f"Part 2: {sim_score}")