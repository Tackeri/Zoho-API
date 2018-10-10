__author__ = 'MinterS'

import requests
import json
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Sales_Orders?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "data": [
        {
            "Customer_E_mail": " apiTest@test.com",
            "Customer_ID": "1234",
            "Job_Number": "12d3456",
            "Subject": "New Sales Order - API",
            "Customer_Name": "David Minter",
            "Account_Name": "Minter Co.",
            "Order_Date": "2018-09-30",
            "Due_Date": "2018-11-18",
            "Status": "Requested",
            "Services_to_be_Completeds": "Mowz",
            "Completed_Date": "",
            "Zip_Code": "02420",
            "City": "Lexington",
            "State": "MA",
            "Street_Address": "1455 Massachusetts Ave",
            "Product_Details": [
                {
                    "product":
                    {
                        "id": "3490721000000271069"
                    },
                    "list_price": 250,
                    "quantity": 3,
                    "Discount": 30,
                    "line_tax": [
                        {
                            "percentage": 5,
                            "name": "5 Percent",
                        }
                    ],
                }
            ],
            "Discount": 35,
            "Adjustment": 35,
            "$line_tax": [
                {
                    "percentage": 25,
                    "name": "Sales Tax"
                }
            ]
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