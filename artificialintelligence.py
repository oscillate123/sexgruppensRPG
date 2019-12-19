try:
	import requests
	import webbrowser
	import random
	import json
	from pathlib import Path
	from spotify import spotify
except Exception as e:
	print(e, "run -> 'pip install requests' for dope features")

class AI:

	def __init__(self, hero):
		self.hero = hero

		self.name = "Skynet"
		self.theme_lyrics = f"{self.name}: Dundun dededun Dundun dededun doodoodoo dooo do doo doodoodoo dooo DO deDOO"

		self.temp_fight = True

	def api_theme_song_open_in_browser(self):
		auth = spotify().auth
		headers = spotify().head
		uri_id = "3dAUz8qeUL6pKf6gp6iemq"
		url = f"https://api.spotify.com/v1/tracks/{uri_id}?market=SE"
		response = requests.get(url=url, headers=headers) # api response
		response_json = response.json() # make it json
		theme_song = response_json.get("preview_url") # get the url of the song
		webbrowser.open_new_tab(url=theme_song) # opens a tab and plays the song

	def json_sorter(self, data):
		return json.dumps(data, indent=4, sort_keys=True)

	def test(self):
		pass


if __name__ == "__main__":
	x = AI(hero="hero")

	x.api_theme_song_open_in_browser()