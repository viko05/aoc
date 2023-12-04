def read_input() -> list[dict[str:set]]:
    with open('input.txt') as file:
        cards = []
        for line in file:
            line = line.rstrip()
            winning_yours = line.split(': ')[1]
            winning_yours = winning_yours.replace('  ', ' ')
            winning, yours = winning_yours.split(' | ')
            winning = set(int(n.strip()) for n in winning.strip().split(' '))
            yours = set(int(n.strip()) for n in yours.strip().split(' '))
            cards.append({'winning_numbers': winning, 'numbers': yours})

    return cards


class Solver:
    def __init__(self, cards: list[dict]):
        self.cards = cards

    def solve(self):
        total_points = 0
        for card in self.cards:
            n_winning = len(card['numbers'].intersection(card['winning_numbers']))
            if n_winning:
                points = pow(2, n_winning - 1)
                total_points += points

        return total_points


solver = Solver(cards=read_input())
result = solver.solve()
print(f'Points: {result}')
