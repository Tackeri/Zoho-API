__author__ = 'MinterS'

import requests
import json
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Leads/upsert?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "data": [
       {
           "Company": "Trinidad Productions",
           "Last_Name": "Trini",
           "First_Name": "Paul",
           "Email": "paul@charlie.com",
           "State": "Texas",
           "Lead_Source:": "API",
           "Custom_Number": 1
       },       {
           "Company": "Trinidad Productions",
           "Last_Name": "Trini",
           "First_Name": "Paul",
           "Email": "paul@charlie.com",
           "State": "Texas",
           "Lead_Source:": "API",
           "Custom_Number": 1
       },
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
