def read_input() -> list[str]:
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]
    return lines


class Solver:

    spell_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def __init__(self, lines: list[str]):
        self.lines = lines
        print(lines)

    def solve(self) -> int:
        s = 0
        first = 0
        last = 0
        for input_line in self.lines:
            first_digit = self.first_digit(input_line)
            last_digit = self.first_digit(input_line[::-1])

            first = first_digit['value']
            last = last_digit['value']

            first_spell_digit = self.first_spell_digit(input_line, False)
            last_spell_digit = self.first_spell_digit(input_line, True)

            if first_spell_digit['value']:
                if first_spell_digit['index'] <= first_digit['index']:
                    first = first_spell_digit['value']

            if last_spell_digit['value']:
                if last == 0:
                    last = last_spell_digit['value']
                elif last_spell_digit['index'] >= len(input_line) - 1 - last_digit['index']:
                    last = last_spell_digit['value']

            number_compose = int(f'{first}{last}')
            s += number_compose

        return s

    @staticmethod
    def first_digit(line: str) -> dict:
        found = {'index': 0, 'value': 0}

        for i, symbol in enumerate(line):
            if symbol.isnumeric():
                return {'index': i, 'value': int(symbol)}
        return found

    def first_spell_digit(self, line: str, rev: bool) -> dict:
        found = {

        }

        for n, spell_num in enumerate(self.spell_nums):
            if rev:
                index_found = line.rfind(spell_num)
            else:
                index_found = line.find(spell_num)

            if index_found > -1:
                found[index_found] = n+1

        indexes = found.keys()
        if len(indexes):
            if rev:
                index = max(indexes)
            else:
                index = min(indexes)

            return {'index': index, 'value': found[index]}

        return {'value': 0}


solver = Solver(read_input())

print(solver.solve())
