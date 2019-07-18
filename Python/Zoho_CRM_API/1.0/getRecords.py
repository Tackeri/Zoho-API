__author__ = 'MinterS'

# Zoho CRM API v2.0 - Get Records from Module
# This program will fetch 2 records from one of the following modules:

    # leads, accounts, contacts, deals, 
    # campaigns, tasks, cases, events, 
    # calls, solutions, products, vendors, 
    # pricebooks, quotes, sales_orders, 
    # purchase_orders, invoices, custom, notes, 
    # approvals, dashboards, search and activities.

import requests, json, xml.dom.minidom
import credentials

module = "Leads"

# Call API
url = 'https://crm.zoho.com/crm/private/xml/{module}/getRecords?{token}&scope=crmapi'
url = url.replace('{module}', module)
url = url.replace('{token}', credentials.token)
response = requests.get(url)
status = response.status_code

print (url)
print (status)

if (status == 200):
    # Print JSON
    # jsonData = json.loads(response.text)
    # print (json.dumps(jsonData, sort_keys=True, indent=4))


    # Print XML
    xmlData = xml.dom.minidom.parseString(response.text)
    xmlPretty = xmlData.toprettyxml()
    print (xmlPretty)

else:
    print ('Status Code: ', status)
    print ('')
    print (response.text)