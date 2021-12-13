class Grid:
    def __init__(self, width, height):
        self.g = [['.'] * width for _ in range(height)]

    def mark(self, x, y):
        self.g[y][x] = '#'

    def __str__(self):
        s = ''
        for line in self.g:
            s += ''.join(line)
            s += '\n'

        return s

    def fold_y(self, pos):
        new_g = []

        for offset in range(1, max(pos, len(self.g) - pos)):
            from_row_idx = pos + offset
            to_row_idx = pos - offset

            if to_row_idx >= 0:
                to_row = self.g[to_row_idx]
            else:
                to_row = ['.' for _ in range(len(self.g[0]))]

            if from_row_idx < len(self.g):
                from_row = self.g[from_row_idx]
            else:
                from_row = ['.' for _ in range(len(self.g[0]))]
            
            rrow = []
            for col_idx in range(len(self.g[0])):
                a = from_row[col_idx]
                b = to_row[col_idx]

                c = '#' if a == '#' or b == '#' else '.'
                rrow.append(c)

            new_g = [rrow] + new_g

        self.g = new_g

    def fold_x(self, pos):
        new_g = []

        for offset in range(1, max(pos, len(self.g[0]) - pos)):
            from_col_idx = pos + offset
            to_col_idx = pos - offset
            if to_col_idx >= 0:
                to_col = [r[to_col_idx] for r in self.g]
            else:
                to_col = ['.' for _ in range(len(self.g))]

            if from_col_idx >= len(self.g[0]):
                from_col = ['.' for _ in range(len(self.g))]
            else:
                from_col = [r[from_col_idx] for r in self.g]

            rrow = []
            for row_idx in range(len(self.g)):
                a = from_col[row_idx]
                b = to_col[row_idx]

                c = '#' if a == '#' or b == '#' else '.'
                rrow.append(c)

            new_g.append(rrow)

        rotated_g = []
        for col_idx in range(len(new_g[0])):
            rotated_g.append([r[col_idx] for r in reversed(new_g)])

        self.g = rotated_g

def parse_input(lines):
    dots = []
    blank = 0
    for line in lines:
        blank += 1
        if line == '':
            break

        x, y = [int(z) for z in line.split(',')]

        dots.append((x, y))

    instr = lines[blank:]
    instructions = []
    for i in instr:
        i = i.replace('fold along ', '')
        axis, pos = i.split('=')
        instructions.append((axis, int(pos)))

    return dots, instructions

def part_one(dots, instructions):
    max_x = 0
    max_y = 0

    for x, y in dots:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    g = Grid(max_x + 1, max_y + 1)

    for x, y in dots:
        g.mark(x, y)


    for axis, pos in instructions[:1]:
        if axis == 'x':
            g.fold_x(pos)
        else:
            g.fold_y(pos)

    s = 0
    for r in g.g:
        for x in r:
            if x == '#':
                s += 1

    return s

def part_two(dots, instructions):
    max_x = 0
    max_y = 0

    for x, y in dots:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    g = Grid(max_x+1 , max_y +1)

    for x, y in dots:
        g.mark(x, y)


    for axis, pos in instructions:
        if axis == 'x':
            g.fold_x(pos)
        else:
            g.fold_y(pos)

    s = 0
    for r in g.g:
        for x in r:
            if x == '#':
                s += 1

    return(g.__str__())

if __name__ == '__main__':
    with open('inp.txt') as f:
        dots, instructions = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(dots, instructions))
    print(part_two(dots, instructions))
