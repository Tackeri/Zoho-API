__author__ = 'MinterS'

# Zoho Books API v2.0 - Get Records from Module
# This program will fetch 3 records from the defined module


from Authentication import tokens
from Resources import statusCodes
import requests
import json

organization_id = '676667077'

# Call the API and Print the Response

def getRecords(organization_id):
    url = 'https://books.zoho.com/api/v3/contacts?organization_id={org_id}&per_page=3'
    url = url.replace("{org_id}", organization_id)
    headers = {
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
    # print(jsonData)
    count = len(jsonData['contacts'])
    data = jsonData['contacts']
    i = 0
    print(count)
    while i < count:
        print('-- Contact ' + str(i+1) + ' --')
        print(json.dumps(data[i], sort_keys=True, indent=4))
        i += 1

# Run Program
response = getRecords(organization_id)
if response.status_code == 200:
    printResponse(response)
else:
    print('')
    print(response.status_code)
    print(statusCodes.statusCode(response.status_code))
    print(response.text)