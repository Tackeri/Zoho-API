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
import requests, json, getAuthRefresh

module = 'Deals'

# Call the API and Print the Response


def getRecords(module):
    url = 'https://www.zohoapis.com/crm/v2/{module_id}/3490721000001172199'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/3490721000000519039/Custom_List_History'
    
    url = url.replace("{module_id}", module)
    headers = {
        'Authorization': tokens.getAccess(),
        # 'If-Modified-Since': '2018-10-02T17:38:49-05:00',
        # 'If-Created-Since': '2018-10-22T17:38:49-05:00',
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
    print(json.dumps(jsonData, sort_keys=True, indent=4))


# Run Program
response = getRecords(module)
if response.status_code == 200:
    printResponse(response, module)
else:
    print('')
    print(response.status_code)
    print(statusCodes.statusCode(response.status_code))
    print(response.text)
