__author__ = 'MinterS'

# Zoho Desk API v1.0 - Get Organizations from Desk
# This program will fetch the list of Zoho Desk organizations.

from Authentication import tokens
from Resources import statusCodes
import requests, json

organizationId = '673932772'

# Call the API and Print the Response

def getRecords(organizationId):
    url = 'https://desk.zoho.com/api/v1/agents'
    headers = {
        'orgId': organizationId,
        'Authorization': tokens.getAccess(),
    }
    print('')
    print(url)
    print('')
    print(headers)
    print('')
    # Call API
    response = requests.get(url, headers=headers)
    return response

def printResponse(response):
    jsonData = json.loads(response.text)
    data = jsonData
    count = len(data)
    i = 0
    print(json.dumps(data, sort_keys=True, indent=4))

# Run Program
response = getRecords(organizationId)
if response.status_code == 200:
    printResponse(response)
else:
    print('')
    print(response.status_code)
    print(statusCodes.statusCode(response.status_code))
    print(response.text)
