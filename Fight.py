from Hero import*
from Monsters import*
from dice import*
from Treasure import*

class Fight:
    def __init__(self, hero, monster_one=False, monster_two=False, monster_three=False, monster_four=False):
        self.monster_one = monster_one
        self.monster_two = monster_two
        self.monster_three = monster_three
        self.monster_four = monster_four
        self.hero_index = 99
        self.character_fight_list = []
        self.character_fight_list.append(hero)
        self.next_monster = 100

        self.round = 0
        self.hero_start_score = 0
        self.hero = hero
        self.monster_starts = 0
        self.hero_starts = 0
        self.monster_ag = hero.agility
        self.hero_ag = hero.agility

    def is_hero_ai(self):
        if self.hero != "AI":
            return False
        else:
            return True

    def if_attack_is_greater_than_agility(self):
        if monster_ag > hero_ag:
            return

    def try_to_run(self):
        if monster_ag > hero_ag:
            return

    def hero_special_ability(self):
        return

    def print_all(self):
        for character in f.character_fight_list:
            print(f"StartScore SORTED : {character.start_score}")

        for character in f.character_fight_list:
            #print(type(character))
            print(f"Fighters : {character}")
        #print(f"Index :: {f.find_hero_index()}")

    def player_throw_dice(self):
        pass

    def check_monster_spawn(self):
        if self.monster_one != False:
            self.character_fight_list.append(self.monster_one)
        if self.monster_two != False:
            self.character_fight_list.append(self.monster_two)
        if self.monster_three != False:
            self.character_fight_list.append(self.monster_three)
        if self.monster_four != False:
            self.character_fight_list.append(self.monster_four)

    def who_starts(self):
        for character in self.character_fight_list:
            character.start_score = n_dice(character.initiative)

        f.character_fight_list.sort(key=lambda x: x.start_score, reverse=True)

    def if_draw_on_start(self):
        while self.character_fight_list[0].start_score == self.character_fight_list[1].start_score:
            self.character_fight_list[0].start_score = n_dice(self.character_fight_list[0].initiative)
            self.character_fight_list[1].start_score = n_dice(self.character_fight_list[1].initiative)
            f.character_fight_list.sort(key=lambda x: x.start_score, reverse=True)

    def find_hero_index(self):
        index = 0

        for k in self.character_fight_list:
            if k.__class__.__name__ == "Knight":
                return index
            if k.__class__.__name__ == "Wizard":
                return index
            if k.__class__.__name__ == "Rouge":
                return index
            index += 1

    def find_next_monster(self):
        if self.hero_index == len(self.character_fight_list) - 1:
            self.next_monster = self.hero_index - 1
            return self.next_monster
        else:
            self.next_monster = self.hero_index + 1
            return self.next_monster

    def fight_loop(self):

        index = 0
        attack_power = 0
        agility_power = 0

        while True:
            for i in self.character_fight_list:
                self.hero_index = self.find_hero_index()

                if index == self.hero_index:
                    print("Hero fighting")
                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_next_monster()].agility)

                    if attack_power > agility_power:
                        print(f"Player made damage :: {attack_power - agility_power}")
                        self.character_fight_list[self.find_next_monster()].health -= 1

                    if self.character_fight_list[self.find_next_monster()].health < 1:
                        print("Monster dead")
                        del self.character_fight_list[self.find_next_monster()]
                        self.hero_index = self.find_hero_index()

                else:
                    print("Monster fighting")
                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_hero_index()].agility)

                    if attack_power > agility_power:
                        print(f"Monster made damage :: {attack_power - agility_power}")
                        self.character_fight_list[self.find_hero_index()].health -= 1

                if self.character_fight_list[self.find_hero_index()].health < 1:
                    return False

                if len(self.character_fight_list) == 1:
                    t = Treasure()
                    self.character_fight_list[0].hero_total_loot += t.generate_treasure()
                    return True

                #print(f"First_index :: {index}")
                #print(f"Length :: {len(self.character_fight_list)}")

                if index < len(self.character_fight_list):
                    index += 1

                if index == len(self.character_fight_list):
                    #print(f"Index :: {index}")
                    index = 0
                    #continue

                for character in self.character_fight_list:
                    print(f"HP :: {character.__class__.__name__} : {character.health}")

                #print(f"Heroindex :: {self.hero_index}")
                print("\n/ / / / / / / / /")

if __name__ == "__main__":

    k = Knight("TestHero")

    wins = 0
    losses  = 0

    g = GiantSpider()
    o = Orc()
    s = Skeleton()
    t = Troll()

    f = Fight(k, g, o, s, t)

    f.check_monster_spawn()
    f.who_starts()
    f.if_draw_on_start()

    hero_index = f.find_hero_index()

    print(f"LÄNGDE : {len(f.character_fight_list)}")

    f.print_all()

    #fight_or_run = input("Press 1 to attack and 2 to run")
    #if fight_or_run == '1':

    game_stat = f.fight_loop()

    if game_stat == True:
        print("You won the fight")
        print(k.hero_total_loot)
        wins += 1
    else:
        print("You lost Game over")
        losses += 1
