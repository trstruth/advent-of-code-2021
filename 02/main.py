class Position:
    def __init__(self):
        self.x = 0
        self.depth = 0

    def move(self, direction, length):
        if direction == 'forward':
            self.x += length
        elif direction == 'down':
            self.depth += length
        elif direction == 'up':
            self.depth -= length
        else:
            raise Exception(f'invalid direction: {direction}')

class AimedPosition:

    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0

    def move(self, direction, length):
        if direction == 'forward':
            self.x += length
            self.depth += self.aim * length
        elif direction == 'down':
            self.aim += length
        elif direction == 'up':
            self.aim -= length
        else:
            raise Exception(f'invalid direction: {direction}')


def parse_input(lines):
    result = []
    for x in lines:
        direction, length = x.split(' ')
        length = int(length)
        result.append((direction, length))

    return result

def part_one(lines):
    p = Position()
    for direction, length in lines:
        p.move(direction, length)

    return p.x * p.depth

def part_two(lines):
    p = AimedPosition()

    for direction, length in lines:
        p.move(direction, length)

    return p.x * p.depth

if __name__ == '__main__':
    with open('inp1.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
