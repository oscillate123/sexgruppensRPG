class Character:
    def __init__(self, initiative, health, attack, agility):
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility


class Hero(Character):
    name = ""
    bag = {}

    def __init__(self, name, initiative, health, attack, agility, bag):
        super().__init__(initiative, health, attack, agility)
        self.name = name
        self.bag = bag

    def print_stats(self):
        print("-----------------")
        print(f"  Class : {self.__class__.__name__}  ")
        print("-----------------\n")
        print(f"Initiative : {self.initiative}")
        print(f"Healthpoints : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Agility : {self.agility}")
        print("-----------------\n")

    def special_skill(self):
        pass


class Knight(Hero):
    def special_skill(self):
        print("ShieldBlock")


class Wizard(Hero):
    def special_skill(self):
        print("LightBeem")


class Rouge(Hero):
    def special_skill(self):
        print("CriticalHit")
