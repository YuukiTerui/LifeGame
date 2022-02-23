from world import World


class Simulation:
    def __init__(self, limit, worldsize=5) -> None:
        self.world = World(worldsize)
        self.world.create_random()
        self.generation = 0
        self.generation_limit = limit

    def simulate(self):
        for g in range(1, self.generation_limit):
            self.world.update()
            print(self.world.now)
