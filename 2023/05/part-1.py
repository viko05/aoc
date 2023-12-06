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
                # mappings.append()
                # print('==================== mapping end')
                mappings.append(mapping_list)
            elif line[-4:] == 'map:':
                mapping_list = []
                # print('================= new mapping starts')
            else:
                mapping_list.append([int(n) for n in line.split(' ')])

    return mappings


class Solver:
    def __init__(self, seeds: list[int], maps):
        self.seeds = seeds
        self.maps = maps
        self.lambda_maps = []
        # self.init_mappings()

    def init_mappings(self):
        for mappings in self.maps:
            lambda_map = {}
            for mapping in mappings:
                lambda_map[range(mapping[1], mapping[1] + mapping[2] + 1)] = mapping
            self.lambda_maps.append(lambda_map)
            pass
        pass

    def calc(self, seed: int):
        src = seed + 0
        destination = seed + 0

        for mappings in self.maps:
            for mapping in mappings:
                if mapping[1] <= src < mapping[1] + mapping[2]:
                    delta = mapping[0] - mapping[1]
                    destination = src + delta
                    break
            src = destination + 0

        return destination

    def solve(self) -> int:
        m = float('inf')
        for seed in self.seeds:
            res = self.calc(seed)
            m = min(res, m)
        return m


solver = Solver(read_seeds(), read_maps())
result = solver.solve()
print(f'result = {result}')
