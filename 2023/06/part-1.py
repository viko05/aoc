inp_example = [
    {'time': 7, 'distance': 9},
    {'time': 15, 'distance': 40},
    {'time': 30, 'distance': 200},
]

inp = [
    {'time': 44, 'distance': 277},
    {'time': 89, 'distance': 1136},
    {'time': 96, 'distance': 1890},
    {'time': 91, 'distance': 1768},
]


def distance(t_race: int, t_hold: int) -> int:
    return (t_race - t_hold) * t_hold


def win_options_count(race_time: int, record: int):
    time = int(race_time/2)
    cnt = 0
    while distance(race_time, time) > record:
        r = distance(race_time, time)
        print(f'win time: {time} win result {r}')
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
