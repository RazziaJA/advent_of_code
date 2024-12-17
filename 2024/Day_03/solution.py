import re

text = ''
with open("input.txt") as f:
    text = ''.join(f.readlines())

total = 0
for match in re.finditer(r'mul\((?P<l>\d{1,3}),(?P<r>\d{1,3})\)', text):
    total += int(match.group('l')) * int(match.group('r'))

print(f'Part 1: {total}')


total_2 = 0
do = True
for match in re.finditer(r"mul\((?P<l>\d{1,3}),(?P<r>\d{1,3})\)|do\(\)|don't\(\)", text):
    if (match[0] == "do()"):
        do = True
    elif (match[0] == "don't()"):
        do = False
    elif (do):
        total_2 += int(match.group('l')) * int(match.group('r'))

print(f"Part 2: {total_2}")