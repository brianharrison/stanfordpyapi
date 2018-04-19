#Stanford Computational Journalism API Exercise 1 - Source: USA.GOV API endpoint
#written by Brian Harrison - April 19, 2018 - Python 3.6

import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)
# view the data
print("DATA:\n",data,"\n")
# iterate through dict values in the 'meta' tag
print("LOOPING THROUGH DATA DICTS:")
for x in data['meta'].values():
  print(x)
#iterate through dict items in the 'meta' tag
for x in data['meta'].items():
  print(x)
#iterate through dict items in the 'meta' tag
for x in data['meta'].keys():
  print(x)
print("")

print("SELECTING API ELEMENTS:")
print('A.', data['name'])
print('B.', data['query']['metrics'][0])
print('C.', data['taken_at'])
print('D.', data['meta']['description'])
print('E.', data['data'][0]['active_visitors'])
print('TOC.', ', '.join(data.keys()))

