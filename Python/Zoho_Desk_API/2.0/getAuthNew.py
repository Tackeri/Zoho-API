__author__ = 'MinterS'

### Gets New Access Token
### Collects user and client details from credentials.py
### Calls the Auth API to return Access and Refresh Tokens to token text files

from Authentication import tokens, credentials
from Resources import statusCodes
import requests, json


# Collect Credentials and Build URL
url = 'https://accounts.zoho.com/oauth/v2/token?code={grant_token}&redirect_uri={redirect_uri}&client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code'
url = url.replace("{grant_token}", tokens.getGrantToken())
url = url.replace("{redirect_uri}", credentials.redirect_uri)
url = url.replace("{client_id}", credentials.client_id)
url = url.replace("{client_secret}", credentials.client_secret)

# Call API and Return Status
response = requests.post(url)
status = response.status_code
message = statusCodes.statusCode(status)

# Print Input Data
print ('')
print ('---- Request ----')
print ('URL:', url)

# Parse Response data
json_data = json.loads(response.text)
try:
    error = json_data["error"]
except:
    error = 'None'
try: 
    access = json_data["access_token"]
except: 
    access = ''
try: 
    refresh = json_data["refresh_token"]
except: 
    refresh = ''

# Print Output Data
print ('')
print ('---- Results ----')
if error != 'None':
    print ('Error:', error)
    print (response)
    print (response.text)
else:
    print ('Access:', access)
    print ('Refresh:', refresh)
    # Write Token to File
    tokens.saveAccess(access)
    tokens.saveRefresh(refresh)


