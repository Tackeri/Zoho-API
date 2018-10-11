__author__ = 'MinterS'

import requests
import json
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Contacts?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "data": [
        {
            "First_Name": "ContactFirst",
            "Last_Name": "ContactLast",
            "Email": "New@contact.com"
        }
    ]
}

# Print Input Data
print ('')
print ('---- Request ----')
print ('URL:', url)
print ('Head:', headers)

# Call API
response = requests.post(url, headers=headers, json=body)

# Print Output Data
jsonData = json.loads(response.text)
data = jsonData['data']
print ('')
print ('-- Response --')
print (json.dumps(data, sort_keys=True, indent=4))