__author__ = 'JorgeH'

import requests
import json
import urllib.request
from Authentication import tokens

# Define URL
# The key that appears on the Mockaroo URL at the end must match the API key of the user # noqa
url = 'https://www.zohoapis.com/crm/v2/tasks'
urlMockaroo = 'https://my.api.mockaroo.com/zcrmLCADT.json?key=58fd1ee0'

# Reads the Mockaroo data and loads it into the file
data = urllib.request.urlopen(urlMockaroo).read()
mockData = json.loads(data)

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
# NOTE: The mockData[x] must be iterated through. Currently working on this.
body = {
    "data": [
       mockData[0], mockData[1], mockData[2], mockData[3], mockData[4]
    ]
}

# Print Input Data
print('')
print('---- Request ----')
print('URL:', url)
print('Head:', headers)

# Call API
response = requests.post(url, headers=headers, json=body)

# Print Output Data
if (response.status_code) == 200:
    jsonData = json.loads(response.text)
    data = jsonData['data']
    print('')
    print('-- Response --')
    print(json.dumps(data, sort_keys=True, indent=4))
else:
    print(response.status_code)
    print(response.text)
