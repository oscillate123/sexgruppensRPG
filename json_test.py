import json

with open("json_file\saved_heroes.json", "r") as open_file:
	dict_list = json.load(open_file)
	for dict in dict_list:
		#print(dict)
		for heroes in dict:
			#print(dict.get(heroes).get("Type"))
			#if (dict.get(heroes).get("Type")) == "Rouge":

			#for dict in heroes:
				#print(type(dict))
			pass
