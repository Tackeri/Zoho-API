__author__ = 'MinterS'

# Zoho CRM API v2.0 - Get Records from Module
# This program will fetch 2 records from one of the following modules:

# leads, accounts, contacts, deals,
# campaigns, tasks, cases, events,
# calls, solutions, products, vendors,
# pricebooks, quotes, sales_orders,
# purchase_orders, invoices, custom, notes,
# approvals, dashboards, search and activities.

import requests
import json
import xml.dom.minidom
import credentials

module = "Leads"

xmlData = '<Leads><row no="1"><FL val="Last Name">Minter</FL><FL val="First Name">William</FL><FL val="Lead Source">API</FL><FL val="Email">wminter@minter.info</FL></row></Leads>'

# Call API
url = 'https://crm.zoho.com/crm/private/xml/{module}/insertRecords?{token}&xmlData={xmlData}'
url = url.replace('{module}', module)
url = url.replace('{token}', credentials.token)
url = url.replace('{xmlData}', xmlData)
print(url)


response = requests.post(url)
status = response.status_code


if (status == 200):
    # Print JSON
    # jsonData = json.loads(response.text)
    # print (json.dumps(jsonData, sort_keys=True, indent=4))

    # Print XML
    xmlData = xml.dom.minidom.parseString(response.text)
    xmlPretty = xmlData.toprettyxml()
    print(xmlPretty)

else:
    print('Status Code: ', status)
    print('')
    print(response.text)