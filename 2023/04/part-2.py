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
            cards.append({'winning_numbers': winning, 'numbers': yours, 'copies_number': 1})

    return cards


class Solver:
    def __init__(self, cards: list[dict]):
        self.cards = cards

    def solve(self):
        total_copies = 0
        for i, card in enumerate(self.cards):
            n_winning = len(card['numbers'].intersection(card['winning_numbers']))
            if n_winning:
                for j in range(i + 1, n_winning + i + 1):
                    print(j)
                    self.cards[j]['copies_number'] += card['copies_number']
            total_copies += card['copies_number']

        return total_copies


solver = Solver(cards=read_input())
result = solver.solve()
print(f'Points: {result}')
