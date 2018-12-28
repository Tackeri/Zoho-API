__author__ = 'MinterS'

import json, requests, getAuthRefresh, csv
from Authentication import tokens


module = "Deals"

# Define URL
url = 'https://www.zohoapis.com/crm/bulk/v2/read?'

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Build Body
body = {
    "query": {
        "module": module,
        "page": 1
    }
}

# Print Input Data
print('')
print('---- Request ----')
print('URL:', url)
print('Head:', headers)

# Call API
response = requests.post(url, headers=headers, json=body)

# Print Output Data
jsonData = json.loads(response.text)
print('')
print('-- Response --')
print(json.dumps(jsonData, sort_keys=True, indent=4))


detailsId = jsonData["data"][0]["details"]["id"]
detailsState = jsonData["data"][0]["details"]["state"]
detailsName = jsonData["data"][0]["details"]["created_by"]["name"]
detailsTime = jsonData["data"][0]["details"]["created_time"]

with open("Python/Zoho_CRM_API/2.0/Output/bulkJobs.csv", "w+") as csvfile:
    row = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    row.writerow([module, detailsId, detailsState, detailsName, detailsTime])
