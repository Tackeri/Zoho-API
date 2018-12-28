__author__ = 'MinterS'

import json, requests, getAuthRefresh
from Authentication import tokens

jobId = "3490721000001204003"

# Define URL
url = 'https://www.zohoapis.com/crm/bulk/v2/read/{job_id}'
url = url.replace("{job_id}", jobId)

# Get Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Print Input Data
print('')
print('---- Request ----')
print('URL:', url)
print('Head:', headers)

# Call API
response = requests.get(url, headers=headers)

# Print Output Data
jsonData = json.loads(response.text)
print('')
print('-- Response --')
print(json.dumps(jsonData, sort_keys=True, indent=4))
