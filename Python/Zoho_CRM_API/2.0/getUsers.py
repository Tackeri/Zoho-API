__author__ = 'MinterS'

###
# Runs API 2.0 call to return all Users from CRM.
###

import requests
import json
from Authentication import credentials, tokens
from Resources import statusCodes

# Define URL
url = 'https://www.zohoapis.com/crm/v2/users?type=ActiveUsers'
headers = {'Authorization': tokens.getAccess()}

# Call API
response = requests.get(url, headers=headers)
jsonData = json.loads(response.text)
count = jsonData['info']['count']
data = jsonData['users']

# Print Output
if response.status_code == 200:
    i = 0
    print ('')
    while i < count:
        print ('-- User ' + str(i+1) + ' --')
        print (json.dumps(data[i], sort_keys=True, indent=4))
        # print ('')
        # print ("Name: " + data[i]['full_name'])
        # print ("Email: " + data[i]['email'])
        # print ("Id: " + data[i]['id'])
        print ('')
        i += 1

else:
    print ('')
    print (response.status_code)
    print (statusCodes.statusCode(response.status_code))
    print (response.text)

    # https://zohoapis.com/crm/v2/Events/search?criteria=(Owner.name:equals:Scott)
