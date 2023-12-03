class Grid:
    size = {'x': 10, 'y': 10}

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


def read_input() -> Grid:
    g = Grid()
    with open('input-example.txt') as file:
        for line in file:
            line = line.strip()
            g.add_row(line)

    return g


grid = read_input()
grid.print()
