import faker
import os
import sys

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


if __name__ == '__main__':
    filename, size = None, None
    try:
        filename = sys.argv[1]
        size = int(sys.argv[2])
    except:
        print('You need to pass the filename to create and its size')
        exit(-1)
    make_file(filename, size)
    sorted_file_size = size / 500
    if sorted_file_size < 100:
        sorted_file_size = 100

    os.system('cd ./sorted_files')
    os.system('rm *')
    os.system('cd ..')
    command = f'split --verbose -l{sorted_file_size} {filename} ./sorted_files/sorted_'


    os.system(command)
    # cd sorted_files
    # split --verbose -l70000  ../very_large.txt sorted_
