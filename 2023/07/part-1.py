from functools import cmp_to_key


def read_input() -> dict[str]:
    ord_map = {'A': 'Z', 'K': 'Y', 'Q': 'X', 'J': 'W', 'T': 'V', }
    with open('input.txt') as file:
        lines = {}
        for line in file:
            line = line.rstrip()
            parts = line.split(' ')

            for key in ord_map:
                parts[0] = parts[0].replace(key, ord_map[key])
                parts[0] = ''.join(parts[0])

            lines[parts[0]] = int(parts[1])

    return lines


class Solver:
    def __init__(self, hands: dict):
        self.hands = hands

    def solve(self):
        print(self.hands)
        hands = list(self.hands.keys())
        hands.sort(key=cmp_to_key(self.compare))
        res = 0
        for i, card in enumerate(hands):
            res += (i + 1) * self.hands[card]
        return res

    def compare(self, a: str, b: str):
        set_a = set(a)
        set_b = set(b)

        # Second check
        list_a = sorted(list(set_a), reverse=True)
        list_b = sorted(list(set_b), reverse=True)
        max_n_a = 1
        max_n_b = 1
        str_a = ''
        str_b = ''
        combo_set_a = []
        combo_set_b = []

        for n in reversed(range(1, 6)):
            for card in list_a:
                if a.count(card) == n:
                    max_n_a = max(max_n_a, n)
                    combo_set_a.append(n)
                    str_a += n * card

        for n in reversed(range(1, 6)):
            for card in list_b:
                if b.count(card) == n:
                    max_n_b = max(max_n_b, n)
                    combo_set_b.append(n)
                    str_b += n * card

        if len(combo_set_a) < len(combo_set_b):
            return 1
        elif len(combo_set_a) > len(combo_set_b):
            return -1
        else:
            if max_n_a > max_n_b:
                return 1
            elif max_n_b > max_n_a:
                return -1
            else:
                if a > b:
                    return 1
                elif a < b:
                    return -1
                else:
                    pass

        return 0


solver = Solver(read_input())
result = solver.solve()
print(result)
