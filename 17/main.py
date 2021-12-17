class Probe:
    def __init__(self, x_velocity, y_velocity):
        self.x = 0
        self.y = 0
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def pos(self):
        return (self.x, self.y)

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.x_velocity += 1

        self.y_velocity -= 1

        return self.pos()

def parse_input(lines):
    inp = lines[0]
    inp = inp.split(': ')[1]
    x, y = inp.split(', ')
    x_range = [int(n) for n in x.split('=')[1].split('..')]
    y_range = [int(n) for n in y.split('=')[1].split('..')]

    return sorted(x_range), sorted(y_range)

def run_to_completion(x_vel, y_vel, x_range, y_range):
    p = Probe(x_vel, y_vel)
    points_of_interest = {(0, 0): 'S'}

    success = False
    max_y = float('-inf')

    x1, x2 = x_range
    y1, y2 = y_range

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            points_of_interest[(x, y)] = 'T'

    is_still_above = p.y >= y1
    is_over = x1 <= p.x <= x2
    has_horizontal_velocity = p.x_velocity != 0

    while is_still_above and (is_over or has_horizontal_velocity):
        x, y = p.step()

        is_still_above = y >= y1
        has_horizontal_velocity = p.x_velocity != 0
        is_over = x1 <= p.x <= x2

        points_of_interest[(x, y)] = '#'

        max_y = max(y, max_y)
        success = ((x1 <= x <= x2 and y1 <= y <= y2) or success)

    '''
    xs = [c[0] for c in points_of_interest.keys()]
    ys = [c[1] for c in points_of_interest.keys()]

    for y in range(max(ys), min(ys)-1, -1):
        s = []
        for x in range(min(xs), max(xs)+1):
            s.append(points_of_interest.get((x, y), '.'))

        print(''.join(s))
    '''

    return success, max_y, points_of_interest

def part_one(x_range, y_range):
    m = 0
    for x_vel in range(1, 200):
        for y_vel in range(1, 200):
            success, y, _ = run_to_completion(x_vel, y_vel, x_range, y_range)
            if success:
                m = max(m, y)

    return m


def part_two(x_range, y_range):
    velos = set()

    m = 0
    for x_vel in range(1, 200):
        for y_vel in range(-200, 200):
            success, y, _ = run_to_completion(x_vel, y_vel, x_range, y_range)
            if success:
                velos.add((x_vel, y_vel))

    return len(velos)

if __name__ == '__main__':
    with open('inp.txt') as f:
        x_range, y_range = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(x_range, y_range))
    print(part_two(x_range, y_range))
