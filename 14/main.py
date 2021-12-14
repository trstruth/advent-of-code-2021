import functools
from collections import defaultdict

def parse_input(lines):
    template = lines[0]

    rules = [x.split(' -> ') for x in lines[2:]]

    return template, rules

def part_one(template, rules):

    rules = {x[0]: x[1] for x in rules}

    for _ in range(10):
        r = []
        for idx in range(len(template) - 1):
            substring = template[idx:idx+2]

            if substring in rules:
                r.append(f'{substring[0]}{rules[substring]}')

        r.append(template[-1])
        template = ''.join(r)

    counter = {}
    for c in template:
        if c not in counter:
            counter[c]= 0

        counter[c] += 1

    z = sorted(list(counter.values()))

    return z[-1] - z[0]


def part_two(template, rules):
    counts = defaultdict(int)

    for idx in range(len(template)-1):
        substring = template[idx:idx+2]
        counts[substring] += 1

    rules = {x[0]: x[1] for x in rules}

    for _ in range(40):
        new_counts = defaultdict(int)

        for k, v in counts.items():
            a, b = k[0], k[1]

            new_counts[a + rules[k]] += v
            new_counts[rules[k] + b] += v

        counts = new_counts


    single_counts = defaultdict(int)
    for k, v in counts.items():
        a, b = k[0], k[1]
        single_counts[b] += v

    z = sorted(list(single_counts.values()))

    return z[-1] - z[0]


if __name__ == '__main__':
    with open('inp.txt') as f:
        template, rules = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(template, rules))
    print(part_two(template, rules))
