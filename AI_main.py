try:
	import artificialintelligence
	from map import map as map_file
except Exception as e:
	print(e, "run -> 'pip install requests' for dope features")



# map_size = input("map_size")
map_size = 4
ex_map = map_file.map(grid_size=4)


ex_hero = Knight()

ex_map.update_room(coordinate=[1, 1], update="is_here")

x = AI(hero=ex_hero)

print(x.ai_choice(math_result="dumb_retard_ai"))
print(x.random_map_move())

x.api_theme_song_open_in_browser()