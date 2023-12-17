def read_input() -> list[str]:
    # with open('input-example.txt') as file:
    #     lines = [line.rstrip() for line in file]

    file = open('input.txt')
    inp = file.read()
    strs = []
    for s in inp.split(','):
        strs.append(s)
    return strs


strings = read_input()


def calc_hash_symbol(current_val: int, sym: str):
    ascii_code = ord(sym)
    current_val += ascii_code
    current_val *= 17
    current_val = current_val % 256
    return current_val


def calc_hash_string(s: str):
    result = 0
    for ch in s:
        result = calc_hash_symbol(result, ch)
    return result


summ = 0
inp = read_input()
for s in inp:
    summ += calc_hash_string(s)

print(summ)




