import json
import requests
import webbrowser


class spotify:

	def __init__(self):
		self.auth = "BQDpnme1nZwQK_EyP9jQT8WqG7LIWdX6qoxvsmexYhW9dPqyD1BUKg5qkE2hKRXSSKLP4m7EZXEf_hEtLPHPeDL9hwVfP1u-Jw63ktUcacnlctgNQ3XymEImzVrJTiVw-5XAYfrwGbFss0TbFvHqRpISKUQg8qgqkQk"
		self.head = {
			"Accept": "application/json",
			"Content-Type": "application/json",
			"Authorization": f"Bearer {self.auth}"
		}
		self.playlist_id = "3J24PlSzdkKPu4bqUggCZU"
		self.playlist_url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
		self.playlist = "https://open.spotify.com/embed?uri=spotify%3Aplaylist%3A3J24PlSzdkKPu4bqUggCZU"


	def get_playlist(self):
		play_url = self.playlist_url
		head = self.head
		response = requests.get(url=play_url, headers=head)
		response_json = response.json()
		# print(self.json_sorter(response_json))
		# playlist = response_json.get("preview_url")
		self.playlist = response_json
		items = response_json.get("items")
		

		
		# webbrowser.open_new_tab(url=x.get("preview_url"))

	def json_sorter(self, data):
		return json.dumps(data, indent=4, sort_keys=True)


if __name__ == "__main__":
	x = spotify()
	x.get_playlist()