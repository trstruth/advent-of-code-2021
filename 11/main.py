class Grid:
    def __init__(self, lines):
        self.g = []
        for line in lines:
            self.g.append([int(e) for e in line])

        self.flash_count = 0

        self.flashed = set()

    def __str__(self):
        x = ''
        for row in self.g:
            x += ','.join([str(o) for o in row])
            x += '\n'

        return x

    def step(self):
        flashes = []

        self.flashed = set()

        for i, row in enumerate(self.g):
            for j, o in enumerate(row):
                self.g[i][j] += 1
                if self.g[i][j] == 10:
                    flashes.append((i, j))

        self.flashed.update(flashes)
        s = len(flashes)
        while flashes:
            f = flashes.pop(0)
            new_flashes = self.handle_flash(f)
            s += len(new_flashes)
            flashes.extend(new_flashes)
            self.flashed.update(new_flashes)

        # reset all flashed to 0
        for row_idx, row in enumerate(self.g):
            for col, o in enumerate(row):
                if o >= 10:
                    self.g[row_idx][col] = 0

        return s

    def handle_flash(self, coord):
        new_flashes = []

        for n_coord in self.neighbors(coord):
            x, y = n_coord
            self.g[x][y] += 1
            if self.g[x][y] == 10:
                new_flashes.append(n_coord)

        return new_flashes

    def get(self, coord):
        x, y = coord
        return self.g[x][y]

    def neighbors(self, coord):
        delta_x = [-1, 0, 1]
        delta_y = [-1, 0, 1]
        x, y = coord
        neighb_coords = []
        for dx in delta_x:
            for dy in delta_y:
                if dx == 0 and dy == 0:
                    continue

                new_x = x + dx
                new_y = y + dy

                if new_x < 0 or new_x >= len(self.g):
                    continue

                if new_y < 0 or new_y >= len(self.g[0]):
                    continue

                neighb_coords.append((new_x, new_y))

        return neighb_coords

def parse_input(lines):
    return lines

def part_one(inp):
    g = Grid(inp)
    x = 0
    for _ in range(100):
        x += g.step()

    return x

def part_two(inp):
    g = Grid(inp)
    step_num = 1
    while True:
        g.step()
        if len(g.flashed) == 100:
            return step_num

        step_num += 1



if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
