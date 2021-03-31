import asyncio

import math
import random



class BombDistances:

    def __init__(self):
        self._bomb_distance = []

    def __len__(self):
        return len(self._bomb_distance)

    def is_empty(self):
        return len(self._bomb_distance) == 0

    def add(self, distance):
        self._bomb_distance.append(distance)
        self._bomb_distance.sort()

    def glance(self):
        return self._bomb_distance[0] if len(self._bomb_distance) > 0 else None

    def pop(self):
        return self._bomb_distance.pop(0)


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
            # print(bomb_distances._bomb_distance)
            await asyncio.sleep(1)


class DefenseSystem:
    _miles_per_second = None

    def __init__(self, miles_per_second):
        self._miles_per_second = miles_per_second

    async def start(self):
        import datetime
        start_time = datetime.datetime.now()
        with open("old_approach.csv", 'w') as f:
            while True:
                await asyncio.sleep(1)
                total_distance = 0
                collected = 0
                while not bomb_distances.is_empty() and bomb_distances.glance() + total_distance <= self._miles_per_second:
                    total_distance += bomb_distances.pop()
                    collected += 1
                    if collected > 50:
                        break
                duration = (datetime.datetime.now() - start_time ).total_seconds()

                speed = len(bomb_distances) / duration
                f.write(str(speed))
                f.write('\n')
                print(speed)


                #print(f'heap size: {len(bomb_distances)} collected: {collected} speed: {speed}')


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
