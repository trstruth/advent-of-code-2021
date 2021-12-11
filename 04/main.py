class Tile:
    def __init__(self, num):
        self.num = num
        self.marked = False

class Board:
    def __init__(self, rows):
        self.rows = []
        for row in rows:
            row_nums = row.split(' ')
            self.rows.append([Tile(int(n)) for n in row_nums if n != ''])

    def mark(self, chosen_num):
        for row in self.rows:
            for tile in row:
                if tile.num == chosen_num:
                    tile.marked = True

    def is_complete(self):
        for row in self.rows:
            if all(t.marked for t in row):
                return True

        for col_idx in range(5):
            if all(r[col_idx].marked for r in self.rows):
                return True

        return False

    def unmarked_nums(self):
        ret = []
        for row in self.rows:
            for tile in row:
                if not tile.marked:
                    ret.append(tile.num)

        return ret

def parse_input(lines):
    numbers = [int(x) for x in lines[0].split(',')]

    boards = []
    for idx in range(1, len(lines), 5):
        boards.append((Board(lines[idx:idx+5])))

    return numbers, boards

def part_one(numbers, boards):
    for n in numbers:
        for b in boards:
            b.mark(n)

            if b.is_complete():
                return n * sum(b.unmarked_nums())

def part_two(numbers, boards):
    completed_boards = []
    completed_board_set = set()

    for n in numbers:
        for idx, b in enumerate(boards):
            b.mark(n)

            if b.is_complete() and idx not in completed_board_set:
                completed_board_set.add(idx)
                completed_boards.append(b)

            if len(completed_boards) == len(boards):
                return n * sum(completed_boards[-1].unmarked_nums())

if __name__ == '__main__':
    with open('inp1.txt') as f:
        numbers, boards = parse_input([x.strip('\n') for x in f.readlines() if x != '\n'])

    print(part_one(numbers, boards))
    print(part_two(numbers, boards))
