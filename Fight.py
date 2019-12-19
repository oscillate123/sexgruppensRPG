from Hero import*
from Monsters import*
from dice import*
from Treasure import*
from other_functions import*
from colors import bcolors as c
import time

class Fight:
    def __init__(self, hero, is_Ai=False):
        self.hero_instance = hero
        self.character_fight_list = self.generate_monster()
        self.character_fight_list.append(hero)
        self.who_starts()
        self.if_draw_on_start()
        self.next_monster = 99
        self.hero_index = 99
        self.round = 0
        self.ai_choice_number = 0

        #IF AI MAFAKKA
        self.is_Ai = is_Ai

        self.ai_is_playing = True
        self.game_over = False
        self.escaped = False
        self.hero_winner = False
        self.index = 0

        self.fight_commands = []

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

    def hp_bar(self, character_health):
        str = ''

        for i in range(character_health):
            str +=  'I'

        return c.CVIOLET + str + c.RESET

    def print_all(self):

        all_fighters = '\n'

        chars = ["Wizard", "Knight", "Rouge"]

        for character in self.character_fight_list:
            if character.__class__.__name__ in chars:
                all_fighters += "****************************\n" + " " + character.hero_name + " the " + character.__class__.__name__ + " " + self.hp_bar(character.health) + '\n'

            else:
                all_fighters += "****************************\n" + " " + character.__class__.__name__ + "  " + self.hp_bar(character.health) + '\n'

        print(all_fighters + "****************************\n\n")

        for commands in self.fight_commands:
            print(commands)

    def ai_choice(self):

        value_points = ['1', '2']
        probabilities = [0.8, 0.2]

        ai_choice = random_value = (choice(value_points, p=probabilities))

        return ai_choice

    def generate_monster(self):
        g = GiantSpider()
        o = Orc()
        s = Skeleton()
        t = Troll()

        picked_monsters = []

        monsters = []

        for i in range(4):
            value_points = [g, o, s, t, 'no_monster']
            probabilities = [0.2, 0.15, 0.1, 0.05, 0.5]

            random_value = (choice(value_points, p=probabilities))

            if random_value in monsters:
                continue
            else:
                monsters.append(random_value)

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
            for i in self.character_fight_list:
                #print(self.character_fight_list[self.find_hero_index()].agility)
                self.hero_index = self.find_hero_index()

                #Hero Fighting
                if self.index == self.hero_index:
                    temp_round_counter += 1
                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_next_monster()].agility)

                    if attack_power > agility_power:

                        if self.character_fight_list[self.find_hero_index()].type == "Rouge":
                            if self.character_fight_list[self.find_hero_index()].special_skill() == True:
                                self.fight_commands.append(f"{i.hero_name} made a {c.CYELLOW2}critical{c.RESET} hit\n")
                                self.character_fight_list[self.find_next_monster()].health -= 2
                            else:
                                self.fight_commands.append(f"{i.hero_name} made {c.CYELLOW2}damage{c.RESET}\n")
                                self.character_fight_list[self.find_next_monster()].health -= 1
                        else:
                            self.fight_commands.append(f"{i.hero_name} made {c.CYELLOW2}damage{c.RESET}\n")
                            self.character_fight_list[self.find_next_monster()].health -= 1

                    else:
                        self.fight_commands.append(f"{i.hero_name} {c.CYELLOW + c.CITALIC}missed{c.RESET}\n")

                    if self.character_fight_list[self.find_next_monster()].health < 1:
                        self.fight_commands.append(f"{self.character_fight_list[self.find_next_monster()].__class__.__name__} {c.FAIL}dead{c.RESET}\n")

                        self.character_fight_list[self.find_next_monster()].is_alive = False

                        del self.character_fight_list[self.find_next_monster()]
                        self.hero_index = self.find_hero_index()
                        temp_round_counter -= 1

                #Monster Fighting
                else:
                    temp_round_counter += 1

                    if self.round == 0 and self.character_fight_list[self.find_hero_index()].type == "Knight":
                        self.character_fight_list[self.find_hero_index()].special_skill(self.round)
                        self.fight_commands.append(f"{self.character_fight_list[self.find_hero_index()].hero_name} {c.CYELLOW2}BLOCKED{c.RESET}\n")

                    attack_power = n_dice(i.attack)
                    agility_power = n_dice(self.character_fight_list[self.find_hero_index()].agility)

                    if self.character_fight_list[self.find_hero_index()].type == "Knight":
                        self.character_fight_list[self.find_hero_index()].agility = 4

                    if attack_power > agility_power:
                        self.fight_commands.append(f"{i.__class__.__name__ } made {c.CYELLOW2}damage{c.RESET}\n")
                        self.character_fight_list[self.find_hero_index()].health -= 1
                    else:
                        self.fight_commands.append(f"{i.__class__.__name__ } {c.CYELLOW + c.CITALIC}missed{c.RESET}\n")



                if self.character_fight_list[self.find_hero_index()].health < 1:
                    return 'died'

                if len(self.character_fight_list) == 1:
                    clear_screen()
                    self.print_all()
                    print(c.blink + "You won the fight" + c.RESET)
                    input("Press to continue your journey...")
                    return 'win'

                if self.index < len(self.character_fight_list):
                    self.index += 1

                if self.index == len(self.character_fight_list):
                    self.index = 0

                self.round += 1

                if temp_round_counter == len(self.character_fight_list) and self.is_Ai == False:
                    clear_screen()
                    self.print_all()
                    self.fight_commands = []
                    fight_or_run = input("Press 1 to attack and 2 to run")
                    temp_round_counter = 0

                    if fight_or_run == '2':
                        if self.try_to_run() == True:
                            return 'escaped'

                elif temp_round_counter == len(self.character_fight_list) and self.is_Ai == True:
                    clear_screen()
                    self.print_all()
                    self.fight_commands = []
                    fight_or_run = self.ai_choice()
                    print(f"AI LOOP : {fight_or_run}")
                    temp_round_counter = 0

                    if fight_or_run == '2':
                        if self.try_to_run() == True:
                            return 'escaped'

                    time.sleep(3)

    def run_fight(self):

        can_you_run = ''
        game_stat = ''

        k = self.hero_instance

        # f = Fight(k)

        #If AI == False humans choose to play or run
        if self.is_Ai == False:
            self.print_all()
            fight_or_run = input("Press 1 to attack and 2 to run")

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
        elif self.is_Ai == True:
            self.print_all()
            #game_stat = f.fight_loop()

            fight_or_run = self.ai_choice_number
            print(f"AI main meny :: {fight_or_run}")

            if fight_or_run == '1':
                #input("AI FIGHT")
                game_stat = self.fight_loop()

            elif fight_or_run == '2':
                #input("AI PUSSY GONE")
                can_you_run = self.try_to_run()

        #Outcome for both AI and human player
        if game_stat == 'win':
            #More code here tomorrow
            print("You win the fight")
            return game_stat

        elif game_stat == 'died':
            #More code here tomorrow
            print("You lost Game over")
            return game_stat

        elif game_stat == 'escaped':
            #More code here tomorrow
            print("You escaped")
            return game_stat
