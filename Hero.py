class Hero:
    def __init__(self, hero_name, initiative, health, attack, agility, score):
        self.hero_name = hero_name
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.score = score

    def print_stats(self):
        print("-----------------")
        print(f"Class : {self.__class__.__name__}  ")
        print("-----------------\n")
        print(f"Name : {self.hero_name}\n")
        print(f"Initiative : {self.initiative}")
        print(f"Health : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Agility : {self.agility}")
        print("-----------------\n")

    def special_skill(self, round):
        pass


class Knight(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 5, 9, 6, 4, 0)


    #Blocks the first attack of every battle.
    def special_skill(self, round):
        if round == 1:
            print("ShieldBlock")
            return True
        else:
            return False


class Wizard(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 6, 4, 9, 5, 0)


    #Always 80% chance to escape a battle
    def special_skill(self, round):
        print("LightBeem")


class Rouge(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 7, 5, 5, 7, 0)


    #Critical hit. Have a 25% chance of doing 2x damage every turn.
    def special_skill(self, round):
        print("CriticalHit")
