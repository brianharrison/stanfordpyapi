#Stanford Computational Journalism API Exercise 4 - Source: Spotify API endpoint
#written by Brian Harrison - April 26, 2018 - Python 3.6

import requests
import json

data_url = "http://2015.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)
related = data['artists']
# view the data
print("DATA:\n",data,"\n")
print("A.",len(related))
print("B.",related[4]['name'])
print("C.",related[11]['followers']['total'])
print("D.",','.join(list(related[0]['genres'])))
print("E.",related[-1]['images'][0]['url'])
print("")
# loop through Beyonce related artists
artists = []
for artist in related:
  if 'pop' in artist['genres']:
    artists.append(artist['name'])
for number,artist in enumerate(artists,1):
  print(str(number)+".",artist)
