class Grid:
    size = {'x': 140, 'y': 140}

    def __init__(self):
        self.rows = []
        self.asterix_map = {}

    def get_point(self, x: int, y: int):
        return self.rows[y][x]

    def print(self):
        for y, row in enumerate(self.rows):
            print(' '.join(row))
            for x, point in enumerate(row):
                pass

    def add_row(self, row: str):
        self.rows.append(row)

    def solve(self):
        self.fill_asterix()
        s = 0
        num_start = None
        num_end = None
        num_indicator = False
        for y, row in enumerate(self.rows):
            for x in range(0, self.size['x'] + 2):
                p = row[x]
                if (not num_indicator) and p.isnumeric():
                    num_start = x, y
                    num_indicator = True
                elif num_start and (not p.isnumeric()):
                    num_end = x, y
                    num_indicator = False
                # Num isolated
                if num_start and num_end:
                    try:
                        part = row[num_start[0]:num_end[0]]
                        if self.find_asterix(num_start[0], num_end[0], y, part):
                            print(f'-------{part}-----ok')
                            s += int(part)
                        else:
                            print(f'-------{part}-----fail')
                    except IndexError:
                        print('err IndexError')
                        pass
                    except ValueError:
                        print('err ValueError')
                        pass

                    num_start = None
                    num_end = None
                    num_indicator = False

        return self.calc_gears()

    def fill_asterix(self):
        for y, row in enumerate(self.rows):
            for x, s in enumerate(row):
                if row[x] == '*':
                    self.asterix_map[x, y] = []

    def calc_gears(self):
        s = 0
        for key in self.asterix_map:
            maybe_gear = self.asterix_map[key]
            if len(maybe_gear) == 2:
                s += int(maybe_gear[0]) * int(maybe_gear[1])
        return s

    def find_asterix(self, start, end, row_index, part) -> bool:
        if self.rows[row_index][start-1] == '*':
            self.asterix_map[(start - 1, row_index)].append(part)
        if self.rows[row_index][end] == '*':
            self.asterix_map[(end, row_index)].append(part)

        for y in [row_index - 1, row_index + 1]:
            for x in range(start - 1, end + 1):
                if self.rows[y][x] == '*':
                    self.asterix_map[(x, y)].append(part)

        return False


def read_input() -> Grid:
    g = Grid()
    g.add_row('.' * (g.size['x'] + 2))
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            line = f'.{line}.'
            g.add_row(line)

    g.add_row('.' * (g.size['x'] + 2))
    return g


grid = read_input()
grid.print()
print(grid.solve())
