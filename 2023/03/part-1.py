class Grid:
    size = {'x': 140, 'y': 140}

    def __init__(self):
        self.rows = []

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
                        if self.is_part(num_start[0], num_end[0], y):
                            print(f'-------{row[num_start[0]:num_end[0]]}-----ok')
                            s += int(row[num_start[0]:num_end[0]])
                        else:
                            print(f'-------{row[num_start[0]:num_end[0]]}-----fail')
                    except IndexError:
                        print('err IndexError')
                        pass
                    except ValueError:
                        print('err ValueError')
                        pass

                    num_start = None
                    num_end = None
                    num_indicator = False
        return s

    def is_part(self, start, end, row_index) -> bool:
        if not (self.rows[row_index][start-1] == '.'):
            return True
        if not (self.rows[row_index][end] == '.'):
            return True
        for y in [row_index - 1, row_index + 1]:
            for x in range(start - 1, end + 1):
                if not (self.rows[y][x] == '.'):
                    return True

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
