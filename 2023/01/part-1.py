def read_input() -> list[str]:
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]
    return lines


class Solver:

    def __init__(self, lines: list[str]):
        self.lines = lines
        print(lines)

    def solve(self) -> int:
        s = 0
        for input_line in self.lines:
            first_digit = self.first_digit(input_line)
            last_digit = self.first_digit(input_line[::-1])
            number_compose = int(f'{first_digit}{last_digit}')
            s += number_compose
        return s

    @staticmethod
    def first_digit(line: str) -> int:
        for symbol in line:
            if symbol.isnumeric():
                return int(symbol)
        return 0


solver = Solver(read_input())

print(solver.solve())
