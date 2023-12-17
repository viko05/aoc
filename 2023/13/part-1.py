class Grid:

    def __init__(self):
        self.rows = []
        self.cols = []

    def get_point(self, x: int, y: int):
        return self.rows[y][x]

    def print(self):
        for y, row in enumerate(self.rows):
            print('  '.join(row))
            for x, point in enumerate(row):
                pass

    def add_row(self, row: str):
        self.rows.append(row)

    def add_to_col(self, row):
        for i, ch in enumerate(row):
            try:
                self.cols[i] += ch
            except IndexError:
                self.cols.append('')
                self.cols[i] += ch


def read_input() -> list[Grid]:
    grids = []
    with open('input.txt') as file:
        g = Grid()
        row_i = 0
        for line in file:
            line = line.rstrip()
            if line:
                g.add_row(line)
                row_i += 1
                g.add_to_col(line)
            else:
                grids.append(g)
                g = Grid()
                row_i = 0
        grids.append(g)

    return grids


def scan(rows: list[str]) -> int:
    max_mir_width = 0
    axis = 0
    length = len(rows)
    mir = False
    for i in range(0, length-1):
        if rows[i] == rows[i+1]:
            mir_width = 1
            j = 1
            mir = True
            while i-j >= 0 and i+j+1 < length:
                left_i = i-j
                right_i = i+j+1
                if rows[left_i] == rows[right_i]:
                    mir_width += 1
                    j += 1
                    mir = True
                else:
                    mir = False
                    break

            if mir_width > max_mir_width and mir:
                max_mir_width = mir_width
                axis = i
            if i+j == length-1:
                break
    if max_mir_width:
        return axis+1
    else:
        return 0


grids = read_input()
result = 0
for grid in grids:
    grid.print()
    row_axis_score = scan(grid.rows)
    row_axis_score *= 100

    col_axis_score = scan(grid.cols)
    if row_axis_score:
        print(f'row score: {row_axis_score}')
    if col_axis_score:
        print(f'col score: {col_axis_score}')

    print('')
    result = result + row_axis_score + col_axis_score
print(result)


