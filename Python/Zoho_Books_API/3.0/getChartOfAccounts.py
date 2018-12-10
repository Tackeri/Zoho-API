__author__ = 'MinterS'

# Zoho Books API v2.0 - Get Records from Module
# This program will fetch 3 records from the defined module


from Resources import statusCodes
from Authentication import tokens
import requests
import json

organization_id = '676667077'

# Define URL
url = 'https://books.zoho.com/api/v3/chartofaccounts?organization_id={org_id}'

# Prep Token and Headers
token = tokens.getAccess()
headers = {'Authorization': token}

# Prep URL
url = url.replace("{org_id}", organization_id)

# Print Input Data
print('')
print('---- Request ----')
print('URL:', url)
print('Head:', headers)

# Call API
response = requests.get(url, headers=headers)

# Print Output Data
data = json.loads(response.text)
print('')
print('-- Response --')
print(json.dumps(data, sort_keys=True, indent=4))
