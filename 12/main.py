class Graph:
    def __init__(self, inp):
        self.c = {}

        for line in inp:
            n1, n2 = line.split('-')

            if n1 not in self.c:
                self.c[n1] = []

            if n2 not in self.c:
                self.c[n2] = []

            if n1 != 'end' and n2 != 'start':
                self.c[n1].append(n2)

            if n2 != 'end' and n1 != 'start':
                self.c[n2].append(n1)

        self.unique_paths = set()

    def augment(self, target):
        new_dict = {x: y for x, y in self.c.items()}

        for k, v in self.c.items():
            if k == target:
                new_dict[f'{target}*'] = v

            if target in v:
                new_dict[k] = [x for x in v] + [f'{target}*']

        self.c = new_dict

    def dfs(self, start, visited=set(), accum=''):
        if start == 'end':
            self.unique_paths.add(f'{accum[1:]},end'.replace('*', ''))
            return 1

        paths = 0
        for neighb in self.c[start]:
            if neighb in visited:
                continue

            if neighb.isupper():
                paths += self.dfs(neighb, visited=set(list(visited)), accum=accum+f',{start}')
            else:
                paths += self.dfs(neighb, visited=set(list(visited) + [neighb]), accum=accum+f',{start}')

        return paths

def parse_input(lines):
    return lines

def part_one(inp):
    g = Graph(inp)
    return g.dfs('start', visited=set(['start']))

def part_two(inp):
    nodes = set()
    for line in inp:
        start, finish = line.split('-')
        nodes.add(start)
        nodes.add(finish)

    small_caves = [x for x in nodes if x.islower() and x not in ['start', 'end']] + ['']

    unique_paths = set()
    for sc in small_caves:
        g = Graph(inp)
        g.augment(sc)
        g.dfs('start', visited=set(['start']))
        unique_paths = unique_paths.union(g.unique_paths)

    return len(unique_paths)

if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
