from world import World


class Simulatior:
    def __init__(self, world, limit) -> None:
        self.world = world
        self.world.create_random()
        self.generation = 0
        self.generation_limit = limit

    def simulate(self):
        for g in range(1, self.generation_limit):
            self.world.update()
            yield self.world()
