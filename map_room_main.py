from map_2 import map as map

if __name__ == "__main__":
	map_instance = map()
	map_instance.print_map()
	map_instance.update_room(coordinate=[2, 1], update="finished")
	map_instance.print_map()
	map_instance.update_room(coordinate=[3, 1], update="is_here")
	map_instance.print_map()
	for x in map_instance.nerby_rooms():
		print(x, map_instance.nerby_rooms()[x])