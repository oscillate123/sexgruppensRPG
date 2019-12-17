import time 

time_saved =None
class Hero:
    def __init__(self, hero_name, initiative, health, attack, agility, score, type, time_saved):
        self.hero_name = hero_name
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.score = score
        self.type = type
        self.time_saved = time_saved
        self.dict = {"Initiative": initiative, "Health": health, "Attack": attack, "Score": score, "Type": type, "Time": time_saved}

    def __str__(self):
        return f"\n\nType : {self.type}\nName : {self.hero_name}\nScore : {self.score}\nTime Saved : {self.time_saved}"

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

    def add_hero_dict(self, list):
        list[self.hero_name] = self.dict




class Knight(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 5, 9, 6, 4, 0, "Knight", time_saved)


    #Blocks the first attack of every battle.
    def special_skill(self, round):
        if round == 1:
            print("ShieldBlock")
            return True
        else:
            return False


class Wizard(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 6, 4, 9, 5, 0, "Wizard", time_saved)


    #Always 80% chance to escape a battle
    def special_skill(self, round):
        print("LightBeem")


class Rouge(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 7, 5, 5, 7, 0, "Rouge", time_saved)


    #Critical hit. Have a 25% chance of doing 2x damage every turn.
    def special_skill(self, round):
        print("CriticalHit")

