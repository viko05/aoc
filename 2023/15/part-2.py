def read_input() -> list[str]:
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


class Lens:
    def __init__(self, focal_len: int, label: str):
        self.focal_len = int(focal_len)
        self.label = label

    def stick_label(self, label: str):
        self.label = label


class Box:
    def __init__(self):
        self.lenses = []

    def find_lens(self, label: str)-> int:
        for i, l in enumerate(self.lenses):
            if l.label == label:
                return i
        return -1

    def add_lens(self, lens: Lens):
        self.lenses.append(lens)

    def replace_lens(self, lens: Lens):
        found_i = self.find_lens(lens.label)
        self.lenses[found_i] = lens

    def remove_lens(self, label: str):
        found_i = self.find_lens(label)
        if found_i != -1:
            self.lenses.pop(found_i)


def log_state(box_collection: list[Box]):
    for i, box in enumerate(box_collection):
        if len(box.lenses):
            log_ = f'Box {i}: '
            for j, l in enumerate(box.lenses):
                log_ += f'({j}){l.label}={l.focal_len}  '
            print(log_)


# #######################################################
boxes = []
for i in range(0, 256):
    boxes.append(Box())


for command in read_input():
    print(f'"{command}"')
    if command[-1] == '-':
        label = command[0:-1]
        hash_ = calc_hash_string(label)
        boxes[hash_].remove_lens(label)
    else:
        parts = command.split('=')
        label = parts[0]
        focal_len = parts[1]
        hash_ = calc_hash_string(label)

        if boxes[hash_].find_lens(label) == -1:
            boxes[hash_].add_lens(Lens(focal_len, label))
        else:
            # boxes[hash_].remove_lens(label)
            boxes[hash_].replace_lens(Lens(focal_len, label))

    log_state(boxes)

result = 0
for i, box in enumerate(boxes):
    summ = 0
    if len(box.lenses):
        for j, lens in enumerate(box.lenses):
            summ += (j+1)*lens.focal_len
        summ *= (i+1)
    result += summ
print(result)

