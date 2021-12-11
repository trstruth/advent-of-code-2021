with open('inp1.txt') as f:
    lines = [int(l.strip('\n')) for l in f.readlines()]

example = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def part_one(lines):
    total = 0
    
    cur = lines[0]
    for depth in lines[1:]:
        if depth > cur:
            total += 1
    
        cur = depth

    return total

def part_two(lines):
    total = 0

    for last_idx in range(3, len(lines)):
        first_elem = lines[last_idx - 3]
        last_elem = lines[last_idx]

        if first_elem < last_elem:
            total += 1

    return total

print(part_one(lines))
print(part_two(lines))
