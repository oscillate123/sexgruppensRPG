from numpy.random import choice

class Treasure:
    def __init__(self):
        self.coins = 2
        self.bag_of_gold = 6
        self.jewelry = 10
        self.gem = 14
        self.small_treasure_chest = 20

    def generate_treasure(self):
        total_loot = 0
        picked_points = []

        for i in range(5):
            value_points = [self.coins, self.bag_of_gold, self.jewelry, self.gem, self.small_treasure_chest, 0]
            probabilities = [0.4, 0.2, 0.15, 0.1, 0.05, 0.10]

            random_value = choice(value_points, p=probabilities)

            if random_value in picked_points:
                continue
            else:
                picked_points.append(random_value)
                total_loot += random_value

        return total_loot
