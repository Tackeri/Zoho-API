__author__ = 'MinterS'

import requests, json, getAuthRefresh
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
           "Deal_Name": "Minter - 2018 Dec",
           "Closing_Date": "2018-12-30",
           "Contact_Name":
           {
               "id": "3490721000000613062"
           },
           "Account_Name": {
                "id": "3490721000000519039",
            },
           "Stage": "Value Proposition",
           "Type": "Existing Business",
           "Description:": "API Import Testing Subform Insert",
           "Product_Line_Items": [
                {
                    "Amount": 100,
                    "Item": {
                        "id": "3490721000000271044",
                    },
                    "Quantity": 10,
                },
                {
                    "Amount": 150,
                    "Item": {
                        "id": "3490721000000271045",
                    },
                    "Quantity": 10,
                },
                {
                    "Amount": 200,
                    "Item": {
                        "id": "3490721000000271047",
                    },
                    "Quantity": 10,
                }
            ],
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