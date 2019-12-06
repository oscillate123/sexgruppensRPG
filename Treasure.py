from numpy.random import choice


class Treasure:
    def __init__(self, coins, moneybag, gold, rock, small_treasure_chest):
        self.coins = coins
        self.moneybag = moneybag
        self.gold = gold
        self.rock = gemstone
        self.small_treasure_chest = small_treasure_chest

    def generate_treasure():

        total_loot = 0
        picked_points = []

        for i in range(6):

            value_points = [2, 6, 10, 14, 20, 0]
            probabilities = [0.4, 0.2, 0.15, 0.1, 0.05, 0.10]

            random_value = choice(value_points, p=probabilities)

            print(random_value)

            if random_value in picked_points:
                continue
            else:
                picked_points.append(random_value)
                total_loot += random_value

        print(total_loot)

    def alternative_generate_treasure(self):

            total_loot = 0

            coins = [2, 0]
            probabilities = [0.4, 0.6]
            random_value2 = choice(coins, p=probabilities)
            total_loot += random_value2
            print(random_value2)

            moneybag = [6, 0]
            probabilities = [0.2, 0.8]
            random_value3 = choice(moneybag, p=probabilities)
            total_loot += random_value3
            print(random_value3)

            gold = [10, 0]
            probabilities = [0.15, 0.85]
            random_value4 = choice(gold, p=probabilities)
            total_loot += random_value4
            print(random_value4)

            rock = [14, 0]
            probabilities = [0.1, 0.9]
            random_value5 = choice(rock, p=probabilities)
            total_loot += random_value5
            print(random_value5)

            small_treasure_chest = [20, 0]
            probabilities = [0.05, 0.95]
            random_value6 = choice(small_treasure_chest, p=probabilities)
            total_loot += random_value6
            print(random_value6)

            print(f"TOTAL LOOT : {total_loot}")
