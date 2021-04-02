import faker

MAX_TEXT_SIZE = 70

def make_file(filename, count):
    fake_gen = faker.Faker()
    index = 0
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(f'{fake_gen.text(MAX_TEXT_SIZE).lower()}\n')
            index += 1
            if index % 10000 == 0:
                print(index)


def check_file_sorted(filename):
    previous = None
    with open(filename) as f:
        for line in f.readlines():
            if previous and previous > line:
                return False
            previous = line
    return True



FILENAME = 'large.txt'
if __name__ == '__main__':
    #make_file('large.txt', 20000)
    print(check_file_sorted('sorted.txt'))
