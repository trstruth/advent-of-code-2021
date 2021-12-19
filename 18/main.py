class Snail:
    def __init__(self, x, parent=None):
        self.l = self.r = self.val = None
        self.parent = parent
        self.special = False

        if isinstance(x, list):
            l, r = x
            self.l = Snail(l, parent=self)
            self.r = Snail(r, parent=self)
        else:
            self.val = x

    def is_regular(self):
        return not (self.val is None)

    def is_complete(self):
        return 

    def walk(self):
        s = []
        cur = self
        depth = 0

        while s or cur is not None:
            if cur is not None:
                s.append((cur, depth))
                cur = cur.l
                depth += 1
                continue

            cur, depth = s.pop()
            yield cur, depth

            cur = cur.r

    def explode(self):
        s = []
        cur = self
        depth = 0
        found = None

        while s or cur is not None:
            if cur is not None:
                s.append((cur, depth))
                cur = cur.l
                depth += 1
                continue

            cur, depth = s.pop()

            if depth >= 4 and cur.l is not None and cur.r is not None:
                l, r = cur.l.val, cur.r.val
                parent = cur.parent
                new = Snail(0)
                new.special = True
                new.parent = parent

                if parent.l is cur:
                    found = 'l'
                    runner = parent.r
                    if runner.is_regular():
                        parent.r.val += r
                    else:
                        while not runner.is_regular():
                            runner = runner.l

                        runner.parent.l.val += r
                    parent.l = new
                else:
                    found = 'r'
                    runner = parent.l
                    if runner.is_regular():
                        parent.l.val += l
                    else:
                        while not runner.is_regular():
                            runner = runner.r

                        runner.parent.r.val += l
                    parent.r = new

                break

            cur = cur.r
            depth += 1

        if found is None:
            return False

        nodes = list(self.walk())

        special_idx = None
        for idx, (n, _) in enumerate(nodes):
            if n.special:
                special_idx = idx
                n.special = False
                break

        if found == 'l':
            for n, _ in reversed(nodes[:special_idx]):
                if n.is_regular():
                    parent = n.parent
                    if parent is not None:
                        if parent.l is n:
                            parent.l.val += l
                        else:
                            parent.r.val += l
                    break

        elif found == 'r':
            for n, _ in nodes[special_idx+1:]:
                if n.is_regular():
                    parent = n.parent
                    if parent is not None:
                        if parent.l is n:
                            parent.l.val += r
                        else:
                            parent.r.val += r
                    break

        return True

    def split(self):
        for n, _ in self.walk():
            if not n.is_regular() or n.val < 10:
                continue

            parent = n.parent
            res = self.compute_split(n)
            res.parent = parent

            if parent.l is n:
                parent.l = res
            else:
                parent.r = res

            return True

        return False

    def compute_split(self, n):
        assert n.is_regular()
        a = int(n.val/2)
        return Snail([a, a if n.val % 2 == 0 else a+1])

    def add(self, other):
        n = Snail(None)

        n.l = self
        n.r = other

        self.parent = n
        other.parent = n

        return n

    def deserialize(self):
        if self.is_regular():
            return self.val

        return [self.l.deserialize(), self.r.deserialize()]

    def magnitude(self):
        if self.is_regular():
            return self.val

        return (3 * self.l.magnitude()) + (2 * self.r.magnitude())

def parse_input(lines):
    return [eval(x) for x in lines]

def add(a, b):
    s = a.add(b)

    while True:
        if s.explode():
            continue

        if s.split():
            continue

        break

    return s

def part_one(inp):
    nums = [Snail(x) for x in inp]

    a = nums[0]
    for b in nums[1:]:
        a = add(a, b)

    return a.magnitude()

def part_two(inp):
    m = 0

    for a in inp:
        for b in inp:
            x = Snail(a)
            y = Snail(b)
            m = max(m, add(x, y).magnitude())

            x = Snail(a)
            y = Snail(b)
            m = max(m, add(y, x).magnitude())

    return m

if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
