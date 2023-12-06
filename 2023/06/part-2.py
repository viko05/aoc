inp_example = [
    {'time': 71530, 'distance': 940200},
]

inp = [
    {'time': 44899691, 'distance': 277113618901768},
]


def distance(t_race: int, t_hold: int) -> int:
    return (t_race - t_hold) * t_hold


def win_options_count(race_time: int, record: int):
    time = int(race_time/2)
    cnt = 0
    while distance(race_time, time) > record:
        time -= 1
        cnt += 2

    if race_time % 2 == 0:
        cnt -= 1

    return cnt


prod = 1
for race in inp:
    win_count = win_options_count(race['time'], race['distance'])
    prod *= win_count

print(prod)
