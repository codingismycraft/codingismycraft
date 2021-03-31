import asyncio
import math
import random

import heap

MinHeap = heap.MinHeap





class BombDistances:

    def __init__(self):
        self._bomb_distance = MinHeap()

    def is_empty(self):
        return len(self._bomb_distance) == 0

    def __len__(self):
        return len(self._bomb_distance)

    def add(self, distance):
        self._bomb_distance.add(distance)

    def pop(self):
        return self._bomb_distance.pop()


bomb_distances = BombDistances()


class BombGenerator:
    def __init__(self, frequency):
        self._frequency = frequency

    async def start(self):
        while True:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            bomb_distances.add(int(math.sqrt(x * x + y * y)))
            await asyncio.sleep(self._frequency)

    async def monitor(self):
        while True:
            #print(bomb_distances._bomb_distance._heap)
            await asyncio.sleep(1)


class DefenseSystem:
    _miles_per_second = None

    def __init__(self, miles_per_second):
        self._miles_per_second = miles_per_second

    async def start(self):
        import datetime

        start_time = datetime.datetime.now()
        with open("new_approach.csv", 'w') as f:
            while True:
                await asyncio.sleep(0.2)
                total_distance = 0
                collected = []
                while not bomb_distances.is_empty():
                    dist = bomb_distances.pop()

                    if total_distance + dist > self._miles_per_second:
                        bomb_distances.add(dist)
                        break
                    else:
                        collected.append(dist)
                        total_distance += dist

                duration = (datetime.datetime.now() - start_time).total_seconds()

                speed = len(bomb_distances) / duration

                f.write(str(speed))
                f.write('\n')
                print(f"Total items collected: {len(collected)} ", sum(collected), f'heap size: {len(bomb_distances)} speed: {speed}')



class World:
    def __init__(self, defence_system, bomb_generator):
        self._defence_system = defence_system
        self._bomb_generator = bomb_generator

    async def start(self):
        asyncio.ensure_future(self._bomb_generator.start())
        asyncio.ensure_future(self._bomb_generator.monitor())
        asyncio.ensure_future(self._defence_system.start())
        while True:
            await asyncio.sleep(0.001)


if __name__ == '__main__':
    bomb_generator = BombGenerator(frequency=0.00001)
    defence_system = DefenseSystem(miles_per_second=1000)
    world = World(defence_system=defence_system, bomb_generator=bomb_generator)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(world.start())
