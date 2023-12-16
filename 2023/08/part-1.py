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

    def solve(self):
        pointer = 'AAA'
        counter = 0
        reset_count = len(self.commands)
        while not pointer == 'ZZZ':
            i = counter % reset_count
            command = self.commands[i]
            pointer = self.move_map[pointer][command]
            counter += 1
            pass
        return counter


solver = Solver(read_commands(), read_map())
res = solver.solve()
print(res)
