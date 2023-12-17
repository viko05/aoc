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


smudge_cleaned = False
smudge_point = tuple()


def scan(rows: list[str]) -> int:
    global smudge_cleaned
    global smudge_point
    smudge_point = tuple()
    max_mir_width = 0
    axis = 0
    length = len(rows)
    for i in range(0, length-1):
        if cmp_with_smudge(rows[i], rows[i+1]):
            mir_width = 1
            j = 1
            mir = True
            while i-j >= 0 and i+j+1 < length:
                left_i = i-j
                right_i = i+j+1
                if cmp_with_smudge(rows[left_i], rows[right_i]):
                    mir_width += 1
                    j += 1
                    mir = True
                else:
                    mir = False
                    smudge_cleaned = False
                    break

            if mir_width > max_mir_width and mir and smudge_cleaned:
                max_mir_width = mir_width
                axis = i
                smudge_cleaned = False

    if max_mir_width:
        return axis+1
    else:
        smudge_cleaned = False
        return 0


def change_symbol(str_row, letter, index):
    return str_row[:index] + letter + str_row[index+1:]


def cmp_with_smudge(row_a: str, row_b: str):
    global smudge_cleaned
    global smudge_point
    diff_count = 0
    for i in range(0, len(row_a)):
        if row_a[i] != row_b[i]:
            diff_count += 1
    if diff_count == 0:
        return True
    if diff_count == 1 and not smudge_cleaned:
        smudge_cleaned = True
        return True
    return False


grids = read_input()
result = 0
counter = 0
for grid in grids:
    grid.print()
    row_axis_score = scan(grid.rows)
    row_axis_score *= 100

    if not smudge_cleaned:
        col_axis_score = scan(grid.cols)
    else:
        col_axis_score = 0

    if row_axis_score:
        print(f'row score: {row_axis_score}')
    if col_axis_score:
        print(f'col score: {col_axis_score}')
    print(f'iter: {counter}')
    smudge_cleaned = False

    print('')
    counter += 1

    result = result + row_axis_score + col_axis_score
print(result)


