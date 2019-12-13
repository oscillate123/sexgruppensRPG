
class Monster:
    def __init__(self, Initiative, health, attack, agility, vanlighet):
        self.Initiative = Initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.vanlighet = vanlighet

class GiantSpider(Monster):
    def __init__(self):
        super().__init__(7, 1, 2, 3, 20)


class Skeletton(Monster):
    def __init__(self):
        super().__init__(4, 2, 3, 3, 15)


class Orc(Monster):
    def __init__(self):
        super().__init__(6, 3, 4, 4, 10)
    pass

class Troll(Monster):
    def __init__(self):
        super().__init__(2, 4, 7, 2, 5)
    pass
