from Hero import*
from Monsters import*
from dice import*
from Treasure import*

class Fight:
    def __init__(self, hero):
        self.character_fight_list = self.generate_monster()
        self.character_fight_list.append(hero)
        self.who_starts()
        self.if_draw_on_start()
        self.next_monster = 99
        self.hero_index = 99
        self.round = 0

        #IF AI MAFAKKA
        self.is_Ai = False

        self.ai_is_playing = True
        self.game_over = False
        self.escaped = False
        self.hero_winner = False
        self.index = 0


    def try_to_run(self):
        escape_procent = self.character_fight_list[self.find_hero_index()].agility * 10

        escape_procent = escape_procent / 100

        if self.character_fight_list[self.find_hero_index()].type == "Wizard":
            escape_procent = self.character_fight_list[self.find_hero_index()].special_skill()

        rest_procent = 1 - escape_procent

        value_points = [True, False]
        probabilities = [escape_procent, rest_procent]

        escape_or_not = choice(value_points, p=probabilities)

        return escape_or_not

    #Debug, remove later + all prints inside fight_loop
    def print_all(self):
        for character in self.character_fight_list:
            print(f"StartScore SORTED : {character.start_score}")

        for character in self.character_fight_list:
            print(f"Fighters : {character}")

    def generate_monster(self):
        g = GiantSpider()
        o = Orc()
        s = Skeleton()
        t = Troll()

        monsters = []

        for i in range(4):
            value_points = [g, o, s, t, 'no_monster']
            probabilities = [0.2, 0.15, 0.1, 0.05, 0.5]

            monsters.append(choice(value_points, p=probabilities))

            for x in monsters:
                if x == 'no_monster':
                    monsters.remove(x)

        return monsters

    def who_starts(self):
        for character in self.character_fight_list:
            character.start_score = n_dice(character.initiative)

        self.character_fight_list.sort(key=lambda x: x.start_score, reverse=True)

    def if_draw_on_start(self):
        if len(self.character_fight_list) > 2:
            while self.character_fight_list[0].start_score == self.character_fight_list[1].start_score:
                self.character_fight_list[0].start_score = n_dice(self.character_fight_list[0].initiative)
                self.character_fight_list[1].start_score = n_dice(self.character_fight_list[1].initiative)

                self.character_fight_list.sort(key=lambda x: x.start_score, reverse=True)

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
        attack_power = 0
        agility_power = 0
        temp_round_counter = 0

        while True:
            print(f"New temp_round_counter ::: {self.round}")
            for i in self.character_fight_list:
                self.hero_index = self.find_hero_index()

                #Hero Fighting
                if self.index == self.hero_index:
                    temp_round_counter += 1
                    print("Hero fighting")
                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_next_monster()].agility)

                    if attack_power > agility_power:
                        print(f"Player made damage :: {attack_power - agility_power}")

                        if self.character_fight_list[self.find_hero_index()].type == "Rouge":
                            if self.character_fight_list[self.find_hero_index()].special_skill() == True:
                                print("CriticalHit")
                                self.character_fight_list[self.find_next_monster()].health -= 2
                        else:
                            self.character_fight_list[self.find_next_monster()].health -= 1

                    if self.character_fight_list[self.find_next_monster()].health < 1:
                        print("Monster dead")
                        del self.character_fight_list[self.find_next_monster()]
                        self.hero_index = self.find_hero_index()

                #Monster Fighting
                else:
                    print("Monster fighting")
                    temp_round_counter += 1

                    if self.round == 0 and self.character_fight_list[self.find_hero_index()].type == "Knight":
                        self.character_fight_list[self.find_hero_index()].special_skill(self.round)

                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_hero_index()].agility)

                    if attack_power > agility_power:
                        print(f"Monster made damage :: {attack_power - agility_power}")
                        self.character_fight_list[self.find_hero_index()].health -= 1

                    self.character_fight_list[self.find_hero_index()].agility = 4

                if self.character_fight_list[self.find_hero_index()].health < 1:
                    return 'died'

                if len(self.character_fight_list) == 1:
                    return 'win'

                if self.index < len(self.character_fight_list):
                    self.index += 1

                if self.index == len(self.character_fight_list):
                    self.index = 0

                #Remove later + prints
                for character in self.character_fight_list:
                    print(f"HP :: {character.__class__.__name__} : {character.health}")

                print("\n/ / / / / / / / /\n")

                self.round += 1

                print(f"Round ::: {self.round}")

                if temp_round_counter == len(self.character_fight_list) and self.is_Ai == False:
                    fight_or_run = input("Press 1 to attack and 2 to run inside loop")
                    temp_round_counter = 0

                    if fight_or_run == '2':
                        if self.try_to_run() == True:
                            return 'escaped'

    def run_fight(self):

        can_you_run = ''
        game_stat = ''

        #k = Knight("TestHero")

        #f = Fight(k)

        print(f"LÄNGD : {len(self.character_fight_list)}")

        self.print_all()

        #If AI == False humans choose to play or run
        if self.is_Ai == False:

            fight_or_run = input("Press 1 to attack and 2 to run main meny")

            #game_stat = True

            if fight_or_run == '1':
                game_stat = self.fight_loop()

            elif fight_or_run == '2':
                can_you_run = self.try_to_run()

                if can_you_run == True:
                    game_stat = 'escaped'
                    

                #If escape fails, players gets to fight shitty monsters
                else:
                    print("NO ESCAPE!")
                    game_stat = self.fight_loop()

        #If AI is True, game runs
        else:
            game_stat = self.fight_loop()

        #Outcome for both AI and human player
        if game_stat == 'win':
            #More code here tomorrow
            print("You won the fight")
            return game_stat

        elif game_stat == 'died':
            #More code here tomorrow
            print("You lost Game over")
            return game_stat

        elif game_stat == 'escaped':
            #More code here tomorrow
            print("You escaped")
            return game_stat


        print("GAME DONE SKA SNYGGA TILL KODEN IMORRN JAJAJJA")
