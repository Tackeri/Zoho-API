__author__ = 'MinterS'

# Zoho CRM API v2.0 - Get Records from Module
# This program will fetch 2 records from one of the following modules:

# leads, accounts, contacts, deals,
# campaigns, tasks, cases, events,
# calls, solutions, products, vendors,
# pricebooks, quotes, sales_orders,
# purchase_orders, invoices, custom, notes,
# approvals, dashboards, search and activities.

from Authentication import tokens
from Resources import statusCodes
import requests
import json

module = 'Portals'

# Call the API and Print the Response


def getRecords(module):
    url = 'https://projectsapi.zoho.com/restapi/portals/'
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


def printResponse(response, module):
    jsonData = json.loads(response.text)

    data = jsonData['portals']
    count = len(data)
    i = 0
    while i < count:
        print('-- ' + module.capitalize() + ' ' + str(i+1) + ' --')
        print(json.dumps(data[i], sort_keys=True, indent=4))
        i += 1


# Run Program
response = getRecords(module)
if response.status_code == 200:
    printResponse(response, module)
else:
    print('')
    print(response.status_code)
    print(statusCodes.statusCode(response.status_code))
    print(response.text)
