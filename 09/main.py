import operator

class HeightMap:
    def __init__(self, m):
        self.m = m

        self.visited = []
        for i in range(len(self.m)):
            row = []
            for j in range(len(self.m[0])):
                row.append(self.m[i][j] == 9)
            self.visited.append(row)

    def at(self, i, j):
        return self.m[i][j]

    def is_visited(self, i, j):
        return self.visited[i][j]

    def visit(self, i, j):
        self.visited[i][j] = True

    def neighbors(self, i, j):
        neighb_coords = filter(lambda c: c[0] >=0 and c[0] < len(self.m) and c[1] >= 0 and c[1] < len(self.m[0]), [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        return [self.at(i, j) for i, j in neighb_coords]

    def neighbor_coords(self, i, j):
        neighb_coords = filter(lambda c: c[0] >=0 and c[0] < len(self.m) and c[1] >= 0 and c[1] < len(self.m[0]), [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        return [(i, j) for i, j in neighb_coords]

    def basin_size(self, i, j):
        size = 0

        q = [(i, j)]
        while q:
            size += 1
            self.visit(i, j)
            i, j = q.pop(0)

            for neighb in self.neighbor_coords(i, j):
                if self.is_visited(*neighb):
                    continue
                self.visit(*neighb)
                q.append(neighb)

        return size

def parse_input(lines):
    return [[int(x) for x in line] for line in lines]

def part_one(heightmap):
    hm = HeightMap(heightmap)

    ans = 0
    for i in range(len(hm.m)):
        for j in range(len(hm.m[0])):
            h = hm.at(i, j)
            if all(h < x for x in hm.neighbors(i, j)):
                ans += (h+1)

    return ans

def part_two(heightmap):
    hm = HeightMap(heightmap)
    basin_sizes = []
    for i in range(len(hm.m)):
        for j in range(len(hm.m[0])):
            if hm.is_visited(i, j):
                continue

            basin_size = hm.basin_size(i, j)
            basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    x, y, z = basin_sizes[:3]
    return x * y * z

if __name__ == '__main__':
    with open('inp.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
