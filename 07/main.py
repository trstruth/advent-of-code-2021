def parse_input(lines):
    return [int(x) for x in lines[0].split(',')]

def part_one(lines):
    record = float('inf')

    def cost_fn(target_pos, crab):
        return abs(target_pos - crab)

    for target_pos in range(min(lines), max(lines)+1):
        cost = sum(cost_fn(target_pos, crab) for crab in lines)
        if cost < record:
            record = cost

    return record

def part_two(lines):
    record = float('inf')

    def cost_fn(target_pos, crab):
        n = abs(target_pos-crab)
        return int((n*(n+1)) / 2)

    for target_pos in range(min(lines), max(lines)+1):
        cost = sum(cost_fn(target_pos, crab) for crab in lines)
        if cost < record:
            record = cost

    return record

if __name__ == '__main__':
    with open('inp.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
