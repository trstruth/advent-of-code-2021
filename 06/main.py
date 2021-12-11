def parse_input(lines):
    return [int(x) for x in lines[0].split(',')]

def part_one(lines):
    for _ in range(80):
        extension = []
        for idx, fish in enumerate(lines):
            if fish == 0:
                lines[idx] = 6
                extension.append(8)
            else:
                lines[idx] -= 1
        lines.extend(extension)

    return len(lines)


def part_two(lines):
    fish_counts = [0] * 9

    for fish in lines:
        fish_counts[fish] += 1

    for _ in range(256):
        fish_counts = apply_day(fish_counts)

    return sum(fish_counts)

def apply_day(fish_counts):
    r = fish_counts[1:]
    r[6] += fish_counts[0]
    r.append(fish_counts[0])
    return r

if __name__ == '__main__':
    with open('inp1.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines[:]))
    print(part_two(lines[:]))
