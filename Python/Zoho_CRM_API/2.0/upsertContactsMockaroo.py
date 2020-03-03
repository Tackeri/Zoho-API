__author__ = 'JorgeH'

import requests
import json
import urllib.request
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Contacts/upsert'

# NOTE: User must add the URL of the API they created in Mockaroo
urlMockaroo = ''

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
       mockData[0]
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
