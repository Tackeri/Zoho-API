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

module = 'Accounts'

# Call the API and Print the Response


def getRecords(module):
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}?per_page=3'
    url = 'https://www.zohoapis.com/crm/v2/{module_id}/3490721000000519039'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/3490721000000593031/Custom_List_History'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Owner.name:starts_with:Scott)'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Owner.id:equals:3490721000000175021)'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Full_Name:equals:Paul Trinidad)'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Created_By.id:equals:3490721000000253001)'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Custom_Number:greater_than:1)'
    # url = 'https://www.zohoapis.com/crm/v2/{module_id}/search?per_page=3&criteria=(Custom_Date:less_than:2018-10-31T15:00:00-05:00)'
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
