import random

LL_DATA_FILENAME = 'data.txt'
REVERSED_LL_DATA_FILENAME = 'data_reversed.txt'


def make_data(N):
    print("Creating the random list in memory..")
    data = [random.randint(100, 10000000) for _ in range(N)]
    counter = 0
    print(f"Creating {LL_DATA_FILENAME}")
    with open(LL_DATA_FILENAME, 'w') as f:
        for i in data:
            f.write(f"{i}\n")
            counter += 1
            if counter % 1000000 == 0:
                print(counter)

    print(f"Creating {REVERSED_LL_DATA_FILENAME}")
    data.reverse()
    counter = 0
    with open(REVERSED_LL_DATA_FILENAME, 'w') as f:
        for i in data:
            f.write(f"{i}\n")
            counter += 1
            if counter % 1000000 == 0:
                print(counter)
    print("Done.")


if __name__ == '__main__':
    make_data(4000000)
