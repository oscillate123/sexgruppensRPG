
class Hero:
    def __init__(self, name, initiative, health, attack, agility):
        self.name = name
        self.initiativ = initiative
        self.health = healthpoints
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

    def special_skill(self):
        pass

class Knight(Hero):
    #Blocks the first attack of every battle.
    def special_skill(self, round):
        if round == 1:
            print("ShieldBlock")
            return True
        else:
            return False

class Wizard(Hero):
    #Always 80% chance to escape a battle
    def special_skill(self):
        print("LightBeem")

class Rouge(Hero):
    #Critical hit. Have a 25% chance of doing 2x damage every turn.
    def special_skill(self):
        print("CriticalHit")
