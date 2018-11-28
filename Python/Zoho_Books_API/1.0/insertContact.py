__author__ = 'MinterS'

# Zoho Books API v2.0 - Get Records from Module
# This program will fetch 3 records from the defined module


from Resources import statusCodes
import credentials
import requests
import json

organization_id = '676667077'

# Define URL
url = 'https://books.zoho.com/api/v3/contacts?organization_id={org_id}&per_page=3&JSONString={body}'

# Prep Token and Headers
token = credentials.token
headers = {'Authorization': token}

# Prep Body
body = {
    "contact_name": "Advanced and Co",
    "company_name": "Advanced and Co",
    "website": "www.advanced-co.com",
    "contact_type": "customer",
    "is_portal_enabled": False,
    "facebook": "zoho",
    "twitter": "zoho"
}

# Prep URL
url = url.replace("{org_id}", organization_id)
url = url.replace("{body}", str(body))

# Print Input Data
print('')
print('---- Request ----')
print('URL:', url)
print('Head:', headers)

# Call API
response = requests.post(url, headers=headers)

# Print Output Data
data = json.loads(response.text)
print('')
print('-- Response --')
print(json.dumps(data, sort_keys=True, indent=4))
