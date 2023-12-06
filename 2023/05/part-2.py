# I'm not really proud of this approximate approach and know there's better solution
# But it works in my case and I left it as is
def read_seeds() -> list[int]:
    file = open("input/seeds.txt", "r")
    seeds = [int(n) for n in file.readline().split(' ')]
    file.close()
    return seeds


def read_maps() -> list[list]:
    with open('input/maps.txt') as file:
        mappings = []
        mapping_list = []
        for line in file:
            line = line.strip()
            if line == '':
                mappings.append(mapping_list)
            elif line[-4:] == 'map:':
                mapping_list = []
            else:
                mapping_list.append([int(n) for n in line.split(' ')])

    return mappings


class Solver:
    def __init__(self, seeds: list[int], maps):
        self.seeds = seeds
        self.maps = maps
        self.lambda_maps = []

    def calc(self, seed: int):
        src = seed
        destination = seed
        for mappings in self.maps:
            for mapping in mappings:
                if mapping[1] <= src < mapping[1] + mapping[2]:

                    delta = mapping[0] - mapping[1]
                    destination = src + delta
                    break
            src = destination

        return destination

    def solve_approx(self) -> dict:
        m = float('inf')
        seed_wanted = 0
        for i in range(0, len(self.seeds), 2):
            step = 10000

            for seed_n in range(self.seeds[i], self.seeds[i] + self.seeds[i+1] + 1, step):
                res = self.calc(seed_n)
                m = min(res, m)
                if res == m:
                    seed_wanted = seed_n

        return {'location': m, 'seed': seed_wanted}

    def solve(self):
        res_approx = self.solve_approx()
        m = res_approx['location']
        for seed_i in range(res_approx['seed'] - 10001, res_approx['seed']):
            res = self.calc(seed_i)
            m = min(res, m)

        return m


solver = Solver(read_seeds(), read_maps())
result = solver.solve()

print(f'result = {result}')
