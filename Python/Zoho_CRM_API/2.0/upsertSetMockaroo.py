import requests, json, urllib.request
import getAuthRefresh
from Authentication import tokens

# Necessary URLs
url ='https://www.zohoapis.com/crm/v2/{module}/upsert'
urlMockaroo =''

def upsertRecords(url, headers, body, getAuthRefresh):
    # Print Input Data
    print('\n---- Request ----')
    print('URL: ', url)
    print('Head: ', headers)

    # Call API
    response = requests.post(url, headers=headers, json=body)

    # Print Output Data
    if response.status_code == 200:
        jsonData = json.loads(response.text)
        data = jsonData['data']
        print(' \n ---- Response ----')
        print(json.dumps(data, sort_keys=True, indent=4))
    elif response.status_code == 401:
        print(response.status_code)
        print(response.text)
        runAgain = getAuthRefresh
    else:
        print(response.status_code)
        print(response.text)

# Reads the Mockaroo data and loads it into the file
data = urllib.request.urlopen(urlMockaroo).read()
mockData = json.loads(data)

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
# NOTE: The mockData[x] must be iterated through, still haven't been able to figure it out.
body = {
    "data": [
        mockData[0]
    ]
}

# Upsert to the Properties module
url = url.replace('{module}', 'Properties')
upsertRecords(url, headers, body, getAuthRefresh)
url = url.replace('Properties', '{module}')

# Upsert to the Accounts module
url = url.replace('{module}', 'Accounts')
upsertRecords(url, headers, body, getAuthRefresh)
url = url.replace('Accounts', '{module}')

# Upsert to the Contacts module
url = url.replace('{module}', 'Contacts')
upsertRecords(url, headers, body, getAuthRefresh)
url = url.replace('Contacts', '{module}')

url = url.replace('{module}', 'Deals')
upsertRecords(url, headers, body, getAuthRefresh)
