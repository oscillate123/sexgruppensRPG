class Hero:
    def __init__(self):
        self.name = name
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility

    def print_stats(self):
        print("-----------------")
        print(f"  Class : {self.__class__.__name__}  ")
        print("-----------------\n")
        print(f"Initiative : {self.initiative}")
        print(f"Health : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Agility : {self.agility}")
        print("-----------------\n")

    def special_skill(self, round):
        pass

class Knight(Hero):
    def __init__(self, hero_name):
        super().__init__()
        self.name = hero_name
        self.initiative = 5
        self.health = 9
        self.attack = 6
        self.agility = 4

    #Blocks the first attack of every battle.
    def special_skill(self, round):
        if round == 1:
            print("ShieldBlock")
            return True
        else:
            return False

class Wizard(Hero):
    def __init__(self, hero_name):
        super().__init__()
        self.name = hero_name
        self.initiative = 6
        self.health = 4
        self.attack = 9
        self.agility = 5

    #Always 80% chance to escape a battle
    def special_skill(self, round):
        print("LightBeem")

class Rouge(Hero):
    def __init__(self, hero_name):
        super().__init__()
        self.name = hero_name
        self.initiative = 7
        self.health = 5
        self.attack = 5
        self.agility = 7

    #Critical hit. Have a 25% chance of doing 2x damage every turn.
    def special_skill(self, round):
        print("CriticalHit")