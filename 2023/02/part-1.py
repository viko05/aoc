
def read_input() -> dict[int:list]:
    games = []
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]

    for game_id, line in enumerate(lines):
        parts = line.split(': ')

        parts[1].split('; ')
        games.append([])
        game = []
        for cube_set in parts[1].split('; '):
            cube_colors = cube_set.split(', ')
            game_set = {}
            for cube_color in cube_colors:
                number_color = cube_color.split(' ')
                number = int(number_color[0])
                color = number_color[1]
                game_set[color] = number
            game.append(game_set)
        games[game_id] = game

    return games


class Solver:
    possible = {'red': 12, 'green': 13, 'blue': 14}

    def __init__(self, games: dict[int:list]):
        self.games = games

    def solve(self):
        result = 0
        for game_id, game in enumerate(self.games):
            # game_sum = self.game_sum(game)

            print(f'{game_id + 1} check')
            if self.is_possible(game):
                result += game_id + 1
                print(f'possible: {game_id+1}')
            else:
                print(f'impossible: {game_id + 1}')
        return result

    def is_possible(self, one_game):
        for cube_set in one_game:
            for color in cube_set:
                if cube_set[color] > self.possible[color]:
                    return False
        return True


input_data = read_input()
solver = Solver(input_data)
result = solver.solve()
print(f'result = {result}')



