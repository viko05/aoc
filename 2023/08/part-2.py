from math import lcm


def read_commands() -> str:
    file = open('input/lr.txt')
    c = file.readline()
    return c


def read_map() -> dict:
    with open('input/map.txt') as file:
        move_map = {}
        for line in file:
            parts = line.rstrip().split(' = ')
            lr = parts[1].strip('()').split(', ')
            move_map[parts[0]] = {'L': lr[0], 'R': lr[1]}

    return move_map


class Solver:
    def __init__(self, commands: str, move_map: dict):
        self.commands = commands
        self.move_map = move_map
        self.start_points = self.get_start_points()

    def get_start_points(self):
        sp = []
        for point in self.move_map:
            if point[2] == 'A':
                sp.append(point)

        return sp

    def solve(self) -> int:
        counters = []
        reset_count = len(self.commands)
        for sp in self.start_points:
            pointer = sp
            counter = 0
            while True:
                i = counter % reset_count
                pointer = self.move_map[pointer][self.commands[i]]
                counter += 1
                if pointer[2] == 'Z':
                    break
            counters.append(counter)

        result = 1
        for n in counters:
            result = lcm(result, n)

        return result


solver = Solver(read_commands(), read_map())
res = solver.solve()
print(res)
