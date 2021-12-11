class Grid:
    def __init__(self):
        self.rows = [[0] * 1000 for _ in range(1000)]

    def mark(self, point):
        self.rows[point.y][point.x] += 1

    def apply_line(self, line):
        for p in line.coords():
            self.mark(p)

    def overlap_count(self, threshold):
        count = 0
        for row in self.rows:
            for elem in row:
                if elem >= threshold:
                    count += 1

        return count

    def __str__(self):
        lines = []

        for row in self.rows:
            lines.append(' '.join(str(e) for e in row))

        return '\n'.join(lines)

class Point:
    def __init__(self, s):
        x, y = s.split(',')
        self.x = int(x)
        self.y = int(y)

class Line:
    def __init__(self, p1, p2):
        self.head = p1
        self.tail = p2

    def coords(self):
        points = []
        if self.head.x == self.tail.x:
            endpoints = sorted([self.head.y, self.tail.y])
            endpoints[-1] += 1
            for y in range(*endpoints):
                points.append(Point(f'{self.head.x},{y}'))
        elif self.head.y == self.tail.y:
            endpoints = sorted([self.head.x, self.tail.x])
            endpoints[-1] += 1
            for x in range(*endpoints):
                points.append(Point(f'{x},{self.head.y}'))
        else:
            xs = [x for x in range(self.head.x, self.tail.x, 1 if self.tail.x > self.head.x else -1)]
            xs.append(self.tail.x)
            ys = [y for y in range(self.head.y, self.tail.y, 1 if self.tail.y > self.head.y else -1)]
            ys.append(self.tail.y)

            for x, y in zip(xs, ys):
                points.append(Point(f'{x},{y}'))

        return points

def parse_input(lines):
    res = []
    for l in lines:
        [head, _, tail] = l.split(' ')
        res.append(Line(Point(head), Point(tail)))

    return res


def part_one(lines):
    g = Grid()

    for line in lines:
        if line.head.x != line.tail.x and line.head.y != line.tail.y:
            continue

        g.apply_line(line)

    return g.overlap_count(2)


def part_two(lines):
    g = Grid()

    for line in lines:
        g.apply_line(line)

    return g.overlap_count(2)

if __name__ == '__main__':
    with open('inp1.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
