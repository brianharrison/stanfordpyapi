#Stanford Computational Journalism API Exercise 2 - Source: Facebook Graph API endpoint
#written by Brian Harrison - April 19, 2018 - Python 3.6

import requests
import json

data_url = "http://2015.compjour.org/files/code/json-examples/graph.facebook-whitehouse.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)
# view the data
print("DATA:\n",data,"\n")
print('')
print('SELECTING API ELEMENTS')
print('A.',data['checkins'])
print('B.',data['likes'])
print('C.',data['location']['longitude'])
print('D.',data['category_list'][-1]['name'])
