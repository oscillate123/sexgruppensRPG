from artificialintelligence import AI
from map import map
from room import room
from Fight import Fight
from Hero import Hero, Knight, Rouge, Wizard
from Monsters import GiantSpider,Orc,Skeleton,Troll,Orc

# map_size = input("map_size")
map_size = 4
ex_map = map(grid_size=4)

ex_map.update_room(coordinate=[1, 1], update="is_here")

ex_hero = Knight(hero_name="SKYNET")

x = AI(hero_instance=ex_hero, map_instance=ex_map)

print(x.ai_choice(math_result="dumb_retard_ai"))
print(x.map_options())

# x.api_theme_song_open_in_browser()