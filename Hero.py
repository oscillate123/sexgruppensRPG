class Hero:
<<<<<<< HEAD
    def __init__(self, hero_name, initiative, health, attack, agility, score, type):
=======
<<<<<<< HEAD
    def __init__(self, hero_name, initiative, health, attack, agility, score, type):
=======
    def __init__(self, hero_name):
>>>>>>> master
>>>>>>> 6cb9431531615b3fe59ef07328f554caac35304c
        self.hero_name = hero_name
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.score = score
        self.type = type
        self.dict = {"Name": hero_name, "Initiative": initiative, "Health": health, "Attack": attack, "Score": score, "Type": type}

    def __str__(self):
        return f"Type : {self.type}\nName : {self.hero_name}\nScore : {self.score}\n "

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
        list.append(self.dict)




class Knight(Hero):
    def __init__(self, hero_name):
<<<<<<< HEAD
        super().__init__(hero_name, 5, 9, 6, 4, 0, "Knight")

=======
<<<<<<< HEAD
        super().__init__(hero_name, 5, 9, 6, 4, 0, "Knight")

=======
        self.hero_name = hero_name
        self.initiative = 5
        self.health = 9
        self.attack = 6
        self.agility = 4
>>>>>>> master
>>>>>>> 6cb9431531615b3fe59ef07328f554caac35304c

    #Blocks the first attack of every battle.
    def special_skill(self, round):
        if round == 1:
            print("ShieldBlock")
            return True
        else:
            return False


class Wizard(Hero):
    def __init__(self, hero_name):
<<<<<<< HEAD
        super().__init__(hero_name, 6, 4, 9, 5, 0, "Wizard")

=======
<<<<<<< HEAD
        super().__init__(hero_name, 6, 4, 9, 5, 0)

=======
        self.hero_name = hero_name
        self.initiative = 6
        self.health = 4
        self.attack = 9
        self.agility = 5
>>>>>>> master
>>>>>>> 6cb9431531615b3fe59ef07328f554caac35304c

    #Always 80% chance to escape a battle
    def special_skill(self, round):
        print("LightBeem")


class Rouge(Hero):
    def __init__(self, hero_name):
<<<<<<< HEAD
        super().__init__(hero_name, 7, 5, 5, 7, 0, "Rouge")

=======
<<<<<<< HEAD
        super().__init__(hero_name, 7, 5, 5, 7, 0, "Rouge")

=======
        self.hero_name = hero_name
        self.initiative = 7
        self.health = 5
        self.attack = 5
        self.agility = 7
>>>>>>> master
>>>>>>> 6cb9431531615b3fe59ef07328f554caac35304c

    #Critical hit. Have a 25% chance of doing 2x damage every turn.
    def special_skill(self, round):
        print("CriticalHit")

