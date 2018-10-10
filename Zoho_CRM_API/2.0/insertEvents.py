## NOT WORKING

__author__ = 'MinterS'

import requests
import json
from Authentication import tokens

# Define URL
url = 'https://www.zohoapis.com/crm/v2/Events?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "data": [
       {
            "Event_Title": "API-Event",
            "Start_DateTime": "2018-10-29T12:12:00+05:30",
            "End_DateTime": "2018-10-29T14:12:00+05:30",
            "Participants": [
               {
                    "type": "user",
                    "participant": "3490721000000255001"
                },
               {
                    "type": "user",
                    "participant": "3490721000000175021"
                }
            ],
            "Remind_At": "15 mins",
            "Who_Id": "3490721000000203751",
            "Venue": "Austin",
            "$se_module": "Leads",
            "What_Id": "3490721000000267101",
            "$send_notification": True
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