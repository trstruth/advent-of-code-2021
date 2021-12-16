import heapq

class Grid:
    def __init__(self, tiles):
        self.tiles = [[Node(x) for x in row] for row in tiles]

    def get(self, row, col):
        return self.tiles[row][col]

    def neighbors(self, row, col):
        neighbor_idxs = [
                (row-1, col),
                (row+1, col),
                (row, col-1),
                (row, col+1),
                ]

        neighbors = [(r, c) for r, c in neighbor_idxs if r >= 0 and r < len(self.tiles) and c >= 0 and c < len(self.tiles[0])]

        return neighbors

    def find_new_current(self):
        min_dist, cur_min = float('inf'), None
        for row_idx, row in enumerate(self.tiles):
            for col_idx, node in enumerate(row):
                if node.visited:
                    continue
                if node.tentative_distance < min_dist:
                    min_dist = node.tentative_distance
                    cur_min = (row_idx, col_idx)

        return cur_min

class BigGrid:
    def __init__(self, tiles):
        placeholder = [[0] * len(tiles[0]) * 5 for _ in range(len(tiles) * 5)]
        shifter = [1,2,3,4,5,6,7,8,9]

        for row_idx in range(0, len(tiles) * 5, len(tiles)):
            for col_idx in range(0, len(tiles[0]) * 5, len(tiles[0])):
                value_offset = int((row_idx + col_idx) / 10)

                for row_offset, r in enumerate(tiles):
                    for col_offset, value in enumerate(r):
                        value_idx = value - 1
                        new_value = shifter[(value_idx + value_offset) % 9]
                        placeholder[row_idx + row_offset][col_idx + col_offset] = Node(new_value)

        self.tiles = placeholder

        self.h = []

    def __str__(self):
        lines = []
        for row in self.tiles:
            lines.append(''.join([str(n.height) for n in row]))

        return '\n'.join(lines)


    def get(self, row, col):
        return self.tiles[row][col]

    def neighbors(self, row, col):
        neighbor_idxs = [
                (row-1, col),
                (row+1, col),
                (row, col-1),
                (row, col+1),
                ]

        neighbors = [(r, c) for r, c in neighbor_idxs if r >= 0 and r < len(self.tiles) and c >= 0 and c < len(self.tiles[0])]

        return neighbors

class Node:
    def __init__(self, height):
        self.height = height
        self.visited = False
        self.tentative_distance = float('inf')

    def __lt__(self, other):
        return self.height < other.height


def parse_input(lines):
    return [[int(x) for x in row] for row in lines]

def part_one(inp):
    g = Grid(inp)
    g.get(0, 0).tentative_distance = 0

    current = (0, 0)

    while not (g.get(-1, -1).visited):
        current_node = g.get(*current)
        for r, c in g.neighbors(*current):
            neighb = g.get(r, c)
            neighb.tentative_distance = min(neighb.tentative_distance, current_node.tentative_distance + neighb.height)

        current_node.visited = True
        current = g.find_new_current()

    return g.get(-1, -1).tentative_distance

def part_two(inp):
    g = BigGrid(inp)
    g.get(0, 0).tentative_distance = 0

    current = (0, 0)

    h = [(0, current)]

    while h:
        _, current = heapq.heappop(h)
        current_node = g.get(*current)
        if current_node.visited:
            continue

        for r, c in g.neighbors(*current):
            neighb = g.get(r, c)
            neighb.tentative_distance = min(neighb.tentative_distance, current_node.tentative_distance + neighb.height)
            heapq.heappush(h, (neighb.tentative_distance, (r, c)))

        current_node.visited = True

    return g.get(-1, -1).tentative_distance

if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
