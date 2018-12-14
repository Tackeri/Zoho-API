__author__ = 'MinterS'

import requests
import json, getAuthRefresh
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Deals?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "data": [
       {
           "Deal_Name": "NewDealAPI1",
           "Closing_Date": "2018-10-20",
           "Contact_Name":
           {
               "id": "3490721000001130143"
           },
           "Stage": "Qualification",
           "Description:": "API"
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