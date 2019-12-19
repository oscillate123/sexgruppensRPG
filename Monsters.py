
class Monster:
    def __init__(self, initiative, health, attack, agility, appearance):
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.appearance = appearance
        self.is_alive = True

    def print_stats(self):
        print("-----------------")
        print(f"Class : {self.__class__.__name__}  ")
        print("-----------------\n")
        print(f"Initiative : {self.initiative}")
        print(f"Health : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Agility : {self.agility}")
        print(f"Appearance : {self.appearance}%")
        print("-----------------\n")

    def get_stats(self):
        monster_info = {
            "monster": self.__class__.__name__,
            "initiative": self.initiative,
            "health": self.health,
            "attack": self.attack,
            "agility": self.agility,
            "appearance": self.appearance,
            "is_alive": self.is_alive
        }
        return monster_info



class GiantSpider(Monster):
    def __init__(self):
        super().__init__(7, 1, 2, 3, 20)


class Skeleton(Monster):
    def __init__(self):
        super().__init__(4, 2, 3, 3, 15)


class Orc(Monster):
    def __init__(self):
        super().__init__(6, 3, 4, 4, 10)


class Troll(Monster):
    def __init__(self):
        super().__init__(2, 4, 7, 2, 5)
