__author__ = 'MinterS'

import json, requests, getAuthRefresh, time
from Authentication import tokens

jobId = "3490721000001204003"
outFile = "Python/Zoho_CRM_API/2.0/Output/bulkRead_" + jobId + "_" + str(time.time()) + ".zip"

# Define URL
url = 'https://www.zohoapis.com/crm/bulk/v2/read/{job_id}/result'
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

# Output Data
print('')
print('---- Response ----')

with open(outFile, "wb") as output:
    output.write(response.content)

print('File saved: ' + outFile)
print('')