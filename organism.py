class Organism:
    def __init__(self, x, y, power, endurance, speed):
        self.x = x
        self.y = y
        self.power = power
        self.endurance = endurance
        self.speed = speed

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def interact(self, other_organism):
        # Implement interaction logic (e.g., competition, predation)
        pass

    def evolve(self):
        # Implement evolution logic (e.g., mutation, adaptation)
        pass