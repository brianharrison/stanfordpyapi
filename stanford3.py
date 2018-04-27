#Stanford Computational Journalism API Exercise 3 - Source: Google Maps Geocoder API endpoint
#written by Brian Harrison - April 26, 2018 - Python 3.6

import requests
import json

data_url = "http://2015.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)
# view the data
locdata = data['results'][0]
print("DATA:\n",locdata,"\n")
print("A.",locdata['formatted_address'])
print("B.",data['status'])
print("C.",locdata['geometry']['location_type'])
print("D.",locdata['geometry']['location']['lat'])
print("E.",locdata['geometry']['viewport']['southwest']['lng'])
longnames = [locdata['address_components'][0]['long_name'],locdata['address_components'][1]['long_name']]
print("F.",", ".join(longnames))
