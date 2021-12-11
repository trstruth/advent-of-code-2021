matches = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>',
}

scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
}

completion_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
}


def parse_input(lines):
    return lines

def part_one(inp):
    score = 0

    for line in inp:
        if line[0] in scores:
            score += scores[line[0]]
            continue

        stack = [line[0]]

        for c in line:
            if c in matches:
                stack.append(c)
                continue

            if matches[stack[-1]] == c:
                stack.pop()
                continue

            score += scores[c]
            break

    return score


def part_two(inp):

    scores = []
    antidotes = []

    for line in inp:
        antidote = compute_antidote(line)
        if antidote is not None:
            antidotes.append(antidote)

    for antidote in antidotes:
        score = 0
        for c in antidote:
            score *= 5
            score += completion_scores[c]

        scores.append(score)

    return sorted(scores)[int(len(scores)/2)]

def compute_antidote(line):
    if line[0] in scores:
        return None

    stack = [line[0]]

    for c in line[1:]:
        if c in matches:
            stack.append(c)
            continue

        if matches[stack[-1]] == c:
            stack.pop()
        else:
            return None

    return ''.join(reversed([matches[x] for x in stack]))

if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
